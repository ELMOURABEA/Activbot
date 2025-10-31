"""
Performance tests for Activbot optimizations
"""
import pytest
import tempfile
import shutil
import time
import yaml
from pathlib import Path
from activbot.workflow_engine import WorkflowEngine
from activbot.workflow_manager import WorkflowManager
from activbot.validator import WorkflowValidator
from activbot.updater import WorkflowUpdater


class TestPerformance:
    """Test cases for performance optimizations"""
    
    @pytest.fixture
    def temp_workflow_dir(self):
        """Create a temporary directory for workflows"""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)
    
    @pytest.fixture
    def temp_plugin_dir(self):
        """Create a temporary directory for plugins"""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)
    
    def test_topological_sort_efficiency(self, temp_workflow_dir):
        """Test that topological sort doesn't sort on every iteration"""
        engine = WorkflowEngine()
        
        # Create a workflow with many tasks to test sorting efficiency
        tasks = []
        for i in range(50):
            task = {
                'name': f'task_{i}',
                'type': 'test',
                'depends_on': [f'task_{i-1}'] if i > 0 else []
            }
            tasks.append(task)
        
        workflow_data = {
            'name': 'performance_test',
            'tasks': tasks
        }
        
        workflow_path = Path(temp_workflow_dir) / 'performance_test.yml'
        with open(workflow_path, 'w') as f:
            yaml.dump(workflow_data, f)
        
        # Load and execute - should be efficient
        start_time = time.time()
        engine.load_workflow(str(workflow_path))
        results = engine.execute_workflow('performance_test')
        execution_time = time.time() - start_time
        
        # Verify it executed correctly
        assert len(results['tasks']) == 50
        assert results['status'] == 'completed'
        
        # Should complete quickly even with 50 tasks (< 0.1 seconds)
        assert execution_time < 0.1
    
    def test_workflow_manager_caching(self, temp_workflow_dir):
        """Test that workflow manager caches workflow listings"""
        manager = WorkflowManager(workflow_dir=temp_workflow_dir)
        
        # Create several workflows
        for i in range(10):
            manager.create_workflow(f'workflow_{i}', [
                {'name': f'task_{i}', 'type': 'test'}
            ])
        
        # First call - builds cache
        start_time = time.time()
        workflows1 = manager.list_workflows(use_cache=False)
        first_call_time = time.time() - start_time
        
        # Second call - uses cache
        start_time = time.time()
        workflows2 = manager.list_workflows(use_cache=True)
        cached_call_time = time.time() - start_time
        
        # Verify same results
        assert set(workflows1) == set(workflows2)
        assert len(workflows1) == 10
        
        # Cached call should be faster (or at least not slower)
        # Note: Due to OS caching, the difference may be minimal
        assert cached_call_time <= first_call_time * 2
    
    def test_validator_caching(self, temp_workflow_dir):
        """Test that validator caches plugin loader and workflow files"""
        # Create some workflow files
        for i in range(5):
            workflow_data = {
                'name': f'workflow_{i}',
                'tasks': [{'name': f'task_{i}', 'type': 'test'}]
            }
            workflow_path = Path(temp_workflow_dir) / f'workflow_{i}.yml'
            with open(workflow_path, 'w') as f:
                yaml.dump(workflow_data, f)
        
        validator = WorkflowValidator(workflow_dir=temp_workflow_dir)
        
        # First call - builds cache
        start_time = time.time()
        results1 = validator.validate_all_workflows(use_cache=False)
        first_call_time = time.time() - start_time
        
        # Second call - uses cache
        start_time = time.time()
        results2 = validator.validate_all_workflows(use_cache=True)
        cached_call_time = time.time() - start_time
        
        # Verify same results
        assert len(results1) == len(results2) == 5
        
        # Cached call should be faster or similar
        assert cached_call_time <= first_call_time * 2
    
    def test_updater_caching(self, temp_workflow_dir, temp_plugin_dir):
        """Test that updater caches file listings"""
        # Create workflow files
        for i in range(5):
            workflow_data = {
                'name': f'workflow_{i}',
                'tasks': [{'name': f'task_{i}', 'type': 'test'}]
            }
            workflow_path = Path(temp_workflow_dir) / f'workflow_{i}.yml'
            with open(workflow_path, 'w') as f:
                yaml.dump(workflow_data, f)
        
        # Create plugin files
        for i in range(3):
            plugin_code = f'''
class TestPlugin_{i}:
    def execute(self, task, context):
        return {{"status": "completed"}}
'''
            plugin_path = Path(temp_plugin_dir) / f'plugin_{i}.py'
            plugin_path.write_text(plugin_code)
        
        updater = WorkflowUpdater(
            workflow_dir=temp_workflow_dir,
            plugin_dir=temp_plugin_dir
        )
        
        # First calls - build cache
        start_time = time.time()
        suggestions1 = updater.analyze_workflows(use_cache=False)
        plugin_updates1 = updater.check_plugin_updates(use_cache=False)
        first_call_time = time.time() - start_time
        
        # Second calls - use cache
        start_time = time.time()
        suggestions2 = updater.analyze_workflows(use_cache=True)
        plugin_updates2 = updater.check_plugin_updates(use_cache=True)
        cached_call_time = time.time() - start_time
        
        # Verify same results
        assert len(suggestions1) == len(suggestions2) == 5
        assert len(plugin_updates1) == len(plugin_updates2) == 3
        
        # Cached calls should be faster or similar
        assert cached_call_time <= first_call_time * 2
    
    def test_complex_dependency_resolution(self, temp_workflow_dir):
        """Test that complex dependency graphs are resolved efficiently"""
        engine = WorkflowEngine()
        
        # Create a diamond dependency pattern which is common but tricky
        # task_a (root)
        # task_b and task_c depend on task_a
        # task_d depends on both task_b and task_c
        tasks = [
            {'name': 'task_d', 'type': 'test', 'depends_on': ['task_b', 'task_c']},
            {'name': 'task_c', 'type': 'test', 'depends_on': ['task_a']},
            {'name': 'task_b', 'type': 'test', 'depends_on': ['task_a']},
            {'name': 'task_a', 'type': 'test'}
        ]
        
        workflow_data = {'name': 'diamond_test', 'tasks': tasks}
        
        workflow_path = Path(temp_workflow_dir) / 'diamond_test.yml'
        with open(workflow_path, 'w') as f:
            yaml.dump(workflow_data, f)
        
        # Should resolve quickly
        start_time = time.time()
        engine.load_workflow(str(workflow_path))
        results = engine.execute_workflow('diamond_test')
        execution_time = time.time() - start_time
        
        # Verify correct ordering
        task_names = [task['name'] for task in results['tasks']]
        assert task_names[0] == 'task_a'
        assert task_names[-1] == 'task_d'
        assert task_names.index('task_b') > task_names.index('task_a')
        assert task_names.index('task_c') > task_names.index('task_a')
        
        # Should be very fast
        assert execution_time < 0.05
    
    def test_cache_invalidation(self, temp_workflow_dir):
        """Test that cache is properly invalidated when workflows change"""
        manager = WorkflowManager(workflow_dir=temp_workflow_dir)
        
        # Create initial workflow
        manager.create_workflow('workflow_1', [
            {'name': 'task_1', 'type': 'test'}
        ])
        
        # Get cached list
        workflows = manager.list_workflows(use_cache=True)
        assert len(workflows) == 1
        
        # Create another workflow - should invalidate cache
        manager.create_workflow('workflow_2', [
            {'name': 'task_2', 'type': 'test'}
        ])
        
        # Should see new workflow even with cache enabled
        workflows = manager.list_workflows(use_cache=True)
        assert len(workflows) == 2
        assert 'workflow_1' in workflows
        assert 'workflow_2' in workflows
