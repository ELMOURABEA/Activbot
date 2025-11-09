"""
Tests for WorkflowManager
"""
import pytest
import tempfile
import shutil
from pathlib import Path
from activbot.workflow_manager import WorkflowManager


class TestWorkflowManager:
    """Test cases for WorkflowManager"""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for tests"""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)
        
    def test_manager_initialization(self, temp_dir):
        """Test manager can be initialized"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        assert manager is not None
        assert manager.workflow_dir.exists()
        
    def test_create_workflow(self, temp_dir):
        """Test creating a new workflow"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        
        tasks = [
            {'name': 'task1', 'type': 'test'},
            {'name': 'task2', 'type': 'build'}
        ]
        
        workflow = manager.create_workflow('test_workflow', tasks)
        
        assert workflow['name'] == 'test_workflow'
        assert workflow['version'] == '1.0.0'
        assert len(workflow['tasks']) == 2
        assert 'created_at' in workflow
        
        # Check file was created
        workflow_file = Path(temp_dir) / 'test_workflow.yml'
        assert workflow_file.exists()
        
    def test_update_workflow(self, temp_dir):
        """Test updating an existing workflow"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        
        # Create initial workflow
        tasks = [{'name': 'task1', 'type': 'test'}]
        manager.create_workflow('test_workflow', tasks)
        
        # Update the workflow
        updates = {
            'tasks': [
                {'name': 'task1', 'type': 'test'},
                {'name': 'task2', 'type': 'build'}
            ]
        }
        
        updated = manager.update_workflow('test_workflow', updates, 
                                         reason='Added build task')
        
        assert updated['version'] == '1.0.1'
        assert len(updated['tasks']) == 2
        assert 'updated_at' in updated
        assert 'update_history' in updated
        
    def test_generate_workflow_from_requirements(self, temp_dir):
        """Test auto-generating workflow from requirements"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        
        requirements = {
            'name': 'auto_workflow',
            'goals': [
                {'type': 'build', 'description': 'Build the project'},
                {'type': 'test', 'description': 'Run tests', 'depends_on': ['task_1_build']}
            ],
            'constraints': {'timeout': 300}
        }
        
        workflow = manager.generate_workflow_from_requirements(requirements)
        
        assert workflow['name'] == 'auto_workflow'
        assert len(workflow['tasks']) == 2
        assert workflow['metadata']['auto_generated'] is True
        
    def test_validate_workflow(self, temp_dir):
        """Test workflow validation"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        
        # Valid workflow
        valid_workflow = {
            'name': 'valid_workflow',
            'tasks': [{'name': 'task1', 'type': 'test'}]
        }
        
        is_valid, errors = manager.validate_workflow(valid_workflow)
        assert is_valid is True
        assert len(errors) == 0
        
        # Invalid workflow - missing name
        invalid_workflow = {
            'tasks': [{'name': 'task1', 'type': 'test'}]
        }
        
        is_valid, errors = manager.validate_workflow(invalid_workflow)
        assert is_valid is False
        assert len(errors) > 0
        
    def test_list_workflows(self, temp_dir):
        """Test listing workflows"""
        manager = WorkflowManager(workflow_dir=temp_dir)
        
        # Initially empty
        assert manager.list_workflows() == []
        
        # Create some workflows
        manager.create_workflow('workflow1', [{'name': 'task1', 'type': 'test'}])
        manager.create_workflow('workflow2', [{'name': 'task2', 'type': 'build'}])
        
        workflows = manager.list_workflows()
        assert len(workflows) == 2
        assert 'workflow1' in workflows
        assert 'workflow2' in workflows
