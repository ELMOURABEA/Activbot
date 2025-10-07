"""
Example Plugin - Demonstrates plugin implementation
"""
from typing import Dict
try:
    from .base_plugin import BasePlugin
except ImportError:
    from activbot.plugins.base_plugin import BasePlugin


class ExamplePlugin(BasePlugin):
    """
    Example plugin demonstrating task execution.
    This plugin can be used as a template for creating new plugins.
    """
    
    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        
    def execute(self, task: Dict, context: Dict) -> Dict:
        """
        Execute an example task.
        
        Args:
            task: Task definition with parameters
            context: Execution context
            
        Returns:
            Execution result
        """
        task_name = task.get('name', 'unnamed')
        parameters = task.get('parameters', {})
        
        # Perform task logic
        result = {
            'name': task_name,
            'type': task.get('type'),
            'status': 'completed',
            'output': f"Executed {task_name} with parameters: {parameters}"
        }
        
        # Add to context for downstream tasks
        context[task_name] = result
        
        return result
        
    def validate_parameters(self, task: Dict) -> tuple[bool, str]:
        """Validate task has required fields."""
        if 'name' not in task:
            return False, "Task must have a 'name' field"
        return True, ""
