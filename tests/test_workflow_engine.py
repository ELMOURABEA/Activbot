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
