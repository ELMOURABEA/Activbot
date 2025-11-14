"""
Base Plugin - Interface for all Activbot plugins
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple


class BasePlugin(ABC):
    """
    Abstract base class for all Activbot plugins.
    Plugins extend the workflow engine with custom task execution logic.
    """
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"
        
    @abstractmethod
    def execute(self, task: Dict, context: Dict) -> Dict:
        """
        Execute a task with the given context.
        
        Args:
            task: Task definition containing parameters
            context: Execution context with shared state
            
        Returns:
            Dict: Execution result with status and output
        """
        pass
        
    def validate_parameters(self, task: Dict) -> Tuple[bool, str]:
        """
        Validate task parameters before execution.
        
        Args:
            task: Task definition to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        return True, ""
        
    def get_info(self) -> Dict[str, Any]:
        """
        Get plugin information.
        
        Returns:
            Dict with plugin metadata
        """
        return {
            'name': self.name,
            'version': self.version,
            'description': self.__doc__ or 'No description'
        }
