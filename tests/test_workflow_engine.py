"""
Tests for WorkflowEngine
"""
import pytest
import tempfile
import yaml
from pathlib import Path
from activbot.workflow_engine import WorkflowEngine


class TestWorkflowEngine:
    """Test cases for WorkflowEngine"""
    
    def test_engine_initialization(self):
        """Test engine can be initialized"""
        engine = WorkflowEngine()
        assert engine is not None
        assert len(engine.workflows) == 0
        assert len(engine.plugins) == 0
        
    def test_load_workflow(self):
        """Test loading a workflow from file"""
        engine = WorkflowEngine()
        
        # Create a temporary workflow file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_workflow',
                'tasks': [
                    {'name': 'task1', 'type': 'test'}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            # Load the workflow
            workflow = engine.load_workflow(temp_path)
            
            assert workflow['name'] == 'test_workflow'
            assert len(workflow['tasks']) == 1
            assert 'test_workflow' in engine.workflows
        finally:
            Path(temp_path).unlink()
            
    def test_load_nonexistent_workflow(self):
        """Test loading a nonexistent workflow raises error"""
        engine = WorkflowEngine()
        
        with pytest.raises(FileNotFoundError):
            engine.load_workflow('/nonexistent/path.yml')
            
    def test_execute_workflow(self):
        """Test executing a simple workflow"""
        engine = WorkflowEngine()
        
        # Create and load a workflow
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_workflow',
                'tasks': [
                    {'name': 'task1', 'type': 'test'},
                    {'name': 'task2', 'type': 'test'}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            engine.load_workflow(temp_path)
            
            # Execute the workflow
            results = engine.execute_workflow('test_workflow')
            
            assert results['workflow'] == 'test_workflow'
            assert results['status'] == 'completed'
            assert len(results['tasks']) == 2
        finally:
            Path(temp_path).unlink()
            
    def test_register_plugin(self):
        """Test registering a plugin"""
        engine = WorkflowEngine()
        
        class TestPlugin:
            def execute(self, task, context):
                return {'status': 'completed', 'plugin': 'test'}
                
        plugin = TestPlugin()
        engine.register_plugin('custom', plugin)
        
        assert 'custom' in engine.plugins
        assert engine.plugins['custom'] == plugin
        
    def test_list_workflows(self):
        """Test listing loaded workflows"""
        engine = WorkflowEngine()
        
        assert engine.list_workflows() == []
        
        # Add a workflow to the engine directly
        engine.workflows['workflow1'] = {'name': 'workflow1'}
        engine.workflows['workflow2'] = {'name': 'workflow2'}
        
        workflows = engine.list_workflows()
        assert len(workflows) == 2
        assert 'workflow1' in workflows
        assert 'workflow2' in workflows
        
    def test_execute_workflow_with_dependencies(self):
        """Test executing a workflow respects task dependencies"""
        engine = WorkflowEngine()
        
        # Create a workflow where tasks are listed out of dependency order
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_deps',
                'tasks': [
                    {'name': 'task_c', 'type': 'test', 'depends_on': ['task_a', 'task_b']},
                    {'name': 'task_a', 'type': 'test'},
                    {'name': 'task_b', 'type': 'test', 'depends_on': ['task_a']}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            engine.load_workflow(temp_path)
            results = engine.execute_workflow('test_deps')
            
            # Verify tasks executed in correct dependency order
            task_names = [task['name'] for task in results['tasks']]
            assert task_names == ['task_a', 'task_b', 'task_c']
            
            # task_a should run first (no dependencies)
            # task_b should run second (depends on task_a)
            # task_c should run last (depends on both)
        finally:
            Path(temp_path).unlink()
            
    def test_execute_workflow_circular_dependency(self):
        """Test that circular dependencies are detected"""
        engine = WorkflowEngine()
        
        # Create a workflow with circular dependencies
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_circular',
                'tasks': [
                    {'name': 'task_a', 'type': 'test', 'depends_on': ['task_b']},
                    {'name': 'task_b', 'type': 'test', 'depends_on': ['task_a']}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            engine.load_workflow(temp_path)
            
            with pytest.raises(ValueError) as exc_info:
                engine.execute_workflow('test_circular')
            
            assert 'Circular dependency' in str(exc_info.value)
        finally:
            Path(temp_path).unlink()
            
    def test_execute_workflow_missing_dependency(self):
        """Test that missing dependencies are detected"""
        engine = WorkflowEngine()
        
        # Create a workflow with missing dependency
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_missing',
                'tasks': [
                    {'name': 'task_a', 'type': 'test'},
                    {'name': 'task_b', 'type': 'test', 'depends_on': ['task_nonexistent']}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            engine.load_workflow(temp_path)
            
            with pytest.raises(ValueError) as exc_info:
                engine.execute_workflow('test_missing')
            
            assert 'non-existent task' in str(exc_info.value)
        finally:
            Path(temp_path).unlink()
            
    def test_execute_workflow_complex_dependencies(self):
        """Test complex dependency graph is resolved correctly"""
        engine = WorkflowEngine()
        
        # Create a workflow with complex dependencies
        # Dependency graph:
        #   task_a (no deps)
        #   task_b (no deps)
        #   task_c -> task_a
        #   task_d -> task_a, task_b
        #   task_e -> task_c, task_d
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            workflow_data = {
                'name': 'test_complex',
                'tasks': [
                    {'name': 'task_e', 'type': 'test', 'depends_on': ['task_c', 'task_d']},
                    {'name': 'task_c', 'type': 'test', 'depends_on': ['task_a']},
                    {'name': 'task_a', 'type': 'test'},
                    {'name': 'task_d', 'type': 'test', 'depends_on': ['task_a', 'task_b']},
                    {'name': 'task_b', 'type': 'test'}
                ]
            }
            yaml.dump(workflow_data, f)
            temp_path = f.name
            
        try:
            engine.load_workflow(temp_path)
            results = engine.execute_workflow('test_complex')
            
            task_names = [task['name'] for task in results['tasks']]
            
            # task_a and task_b must come first (no dependencies)
            assert task_names.index('task_a') < task_names.index('task_c')
            assert task_names.index('task_a') < task_names.index('task_d')
            assert task_names.index('task_b') < task_names.index('task_d')
            
            # task_c must come before task_e
            assert task_names.index('task_c') < task_names.index('task_e')
            
            # task_d must come before task_e
            assert task_names.index('task_d') < task_names.index('task_e')
            
            # task_e must be last
            assert task_names[-1] == 'task_e'
        finally:
            Path(temp_path).unlink()
