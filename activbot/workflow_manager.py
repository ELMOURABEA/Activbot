"""
Workflow Manager - Manages dynamic workflow generation and updates
"""
import yaml
import json
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime, timezone


class WorkflowManager:
    """
    Manages workflow lifecycle including creation, updates, and versioning.
    Enables auto-design and self-evolution of workflows.
    """
    
    def __init__(self, workflow_dir: str = "activbot/workflows"):
        self.workflow_dir = Path(workflow_dir)
        self.workflow_dir.mkdir(parents=True, exist_ok=True)
        self.workflow_history: Dict[str, List[Dict]] = {}
        self._workflow_cache: Optional[List[str]] = None
        self._cache_timestamp: Optional[float] = None
        
    def create_workflow(self, name: str, tasks: List[Dict], 
                       metadata: Optional[Dict] = None) -> Dict:
        """
        Create a new workflow definition dynamically.
        
        Args:
            name: Workflow name
            tasks: List of task definitions
            metadata: Optional metadata
            
        Returns:
            Dict: Created workflow definition
        """
        workflow = {
            'name': name,
            'version': '1.0.0',
            'created_at': datetime.now(timezone.utc).isoformat(),
            'metadata': metadata or {},
            'tasks': tasks
        }
        
        # Save workflow to file
        self._save_workflow(workflow)
        
        # Initialize history
        self.workflow_history[name] = [workflow.copy()]
        
        return workflow
        
    def update_workflow(self, name: str, updates: Dict, 
                       reason: Optional[str] = None) -> Dict:
        """
        Update an existing workflow with new configuration.
        
        Args:
            name: Workflow name to update
            updates: Dictionary of updates to apply
            reason: Optional reason for the update
            
        Returns:
            Dict: Updated workflow definition
        """
        workflow_path = self.workflow_dir / f"{name}.yml"
        
        if not workflow_path.exists():
            raise ValueError(f"Workflow not found: {name}")
            
        # Load current workflow
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
            
        # Store previous version in history
        if name not in self.workflow_history:
            self.workflow_history[name] = []
        self.workflow_history[name].append(workflow.copy())
        
        # Apply updates
        workflow.update(updates)
        
        # Update version and metadata
        version_parts = workflow.get('version', '1.0.0').split('.')
        version_parts[-1] = str(int(version_parts[-1]) + 1)
        workflow['version'] = '.'.join(version_parts)
        workflow['updated_at'] = datetime.now(timezone.utc).isoformat()
        
        if reason:
            if 'update_history' not in workflow:
                workflow['update_history'] = []
            workflow['update_history'].append({
                'version': workflow['version'],
                'timestamp': workflow['updated_at'],
                'reason': reason
            })
            
        # Save updated workflow
        self._save_workflow(workflow)
        
        return workflow
        
    def generate_workflow_from_requirements(self, requirements: Dict) -> Dict:
        """
        Auto-generate a workflow based on requirements specification.
        
        Args:
            requirements: Requirements specification including goals and constraints
            
        Returns:
            Dict: Generated workflow definition
        """
        name = requirements.get('name', 'auto_generated_workflow')
        goals = requirements.get('goals', [])
        constraints = requirements.get('constraints', {})
        
        # Generate tasks based on goals
        tasks = []
        for i, goal in enumerate(goals):
            task = {
                'name': f"task_{i+1}_{goal.get('type', 'generic')}",
                'type': goal.get('type', 'generic'),
                'description': goal.get('description', ''),
                'parameters': goal.get('parameters', {}),
                'depends_on': goal.get('depends_on', [])
            }
            tasks.append(task)
            
        # Create workflow with generated tasks
        metadata = {
            'auto_generated': True,
            'requirements': requirements,
            'constraints': constraints
        }
        
        return self.create_workflow(name, tasks, metadata)
        
    def validate_workflow(self, workflow: Dict) -> tuple[bool, List[str]]:
        """
        Validate a workflow definition against schema and constraints.
        
        Args:
            workflow: Workflow definition to validate
            
        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []
        
        # Check required fields
        if 'name' not in workflow:
            errors.append("Missing required field: 'name'")
            
        if 'tasks' not in workflow:
            errors.append("Missing required field: 'tasks'")
        elif not isinstance(workflow['tasks'], list):
            errors.append("'tasks' must be a list")
            
        # Validate tasks
        if 'tasks' in workflow:
            for i, task in enumerate(workflow['tasks']):
                if not isinstance(task, dict):
                    errors.append(f"Task {i} must be a dictionary")
                    continue
                    
                if 'name' not in task:
                    errors.append(f"Task {i} missing required field: 'name'")
                    
                if 'type' not in task:
                    errors.append(f"Task {i} missing required field: 'type'")
                    
        return len(errors) == 0, errors
        
    def get_workflow_history(self, name: str) -> List[Dict]:
        """
        Get version history for a workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            List of previous workflow versions
        """
        return self.workflow_history.get(name, [])
        
    def _save_workflow(self, workflow: Dict):
        """Save workflow to YAML file."""
        workflow_path = self.workflow_dir / f"{workflow['name']}.yml"
        with open(workflow_path, 'w') as f:
            yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)
        # Invalidate cache when workflow is saved
        self._workflow_cache = None
        self._cache_timestamp = None
            
    def list_workflows(self, use_cache: bool = True) -> List[str]:
        """
        List all available workflow files.
        
        Args:
            use_cache: If True, use cached results if available (default: True)
        
        Returns:
            List of workflow names
        """
        import time
        
        # Check if cache is valid (exists and less than 5 seconds old)
        current_time = time.time()
        if (use_cache and self._workflow_cache is not None and 
            self._cache_timestamp is not None and 
            current_time - self._cache_timestamp < 5):
            return self._workflow_cache.copy()
        
        # Build new list
        workflows = []
        for workflow_file in self.workflow_dir.glob("*.yml"):
            workflows.append(workflow_file.stem)
        
        # Update cache
        self._workflow_cache = workflows
        self._cache_timestamp = current_time
        
        return workflows
