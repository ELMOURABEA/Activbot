"""
Workflow Engine - Core execution engine for dynamic workflows
"""
import yaml
import json
from typing import Dict, List, Any, Optional
from pathlib import Path


class WorkflowEngine:
    """
    Core workflow execution engine that processes workflow definitions
    and executes tasks dynamically.
    """
    
    def __init__(self):
        self.workflows: Dict[str, Dict] = {}
        self.plugins: Dict[str, Any] = {}
        
    def load_workflow(self, workflow_path: str) -> Dict:
        """
        Load a workflow definition from a YAML file.
        
        Args:
            workflow_path: Path to the workflow YAML file
            
        Returns:
            Dict: Parsed workflow definition
        """
        path = Path(workflow_path)
        if not path.exists():
            raise FileNotFoundError(f"Workflow file not found: {workflow_path}")
            
        with open(path, 'r') as f:
            workflow = yaml.safe_load(f)
            
        # Validate basic workflow structure
        if not isinstance(workflow, dict):
            raise ValueError("Workflow must be a dictionary")
            
        if 'name' not in workflow:
            raise ValueError("Workflow must have a 'name' field")
            
        self.workflows[workflow['name']] = workflow
        return workflow
        
    def execute_workflow(self, workflow_name: str, context: Optional[Dict] = None) -> Dict:
        """
        Execute a loaded workflow.
        
        Args:
            workflow_name: Name of the workflow to execute
            context: Optional execution context
            
        Returns:
            Dict: Execution results
        """
        if workflow_name not in self.workflows:
            raise ValueError(f"Workflow not found: {workflow_name}")
            
        workflow = self.workflows[workflow_name]
        context = context or {}
        results = {
            'workflow': workflow_name,
            'status': 'completed',
            'tasks': []
        }
        
        # Execute tasks in the workflow
        for task in workflow.get('tasks', []):
            task_result = self._execute_task(task, context)
            results['tasks'].append(task_result)
            
        return results
        
    def _execute_task(self, task: Dict, context: Dict) -> Dict:
        """
        Execute a single task within a workflow.
        
        Args:
            task: Task definition
            context: Execution context
            
        Returns:
            Dict: Task execution result
        """
        task_name = task.get('name', 'unnamed')
        task_type = task.get('type', 'default')
        
        # Check if a plugin handles this task type
        if task_type in self.plugins:
            return self.plugins[task_type].execute(task, context)
            
        # Default task execution
        return {
            'name': task_name,
            'type': task_type,
            'status': 'completed',
            'output': f"Executed task: {task_name}"
        }
        
    def register_plugin(self, task_type: str, plugin: Any):
        """
        Register a plugin to handle specific task types.
        
        Args:
            task_type: Type of task the plugin handles
            plugin: Plugin instance
        """
        self.plugins[task_type] = plugin
        
    def list_workflows(self) -> List[str]:
        """
        List all loaded workflows.
        
        Returns:
            List[str]: Names of loaded workflows
        """
        return list(self.workflows.keys())
