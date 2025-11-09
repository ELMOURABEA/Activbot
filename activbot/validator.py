"""
Workflow Validator - Validates workflow definitions and compatibility
"""
import sys
import json
from pathlib import Path
from typing import List, Tuple
import yaml

try:
    from jsonschema import validate, ValidationError
except ImportError:
    ValidationError = Exception
    
    def validate(instance, schema):
        """Fallback validation function"""
        pass


class WorkflowValidator:
    """
    Validates workflow definitions against schema and checks compatibility
    with available plugins.
    """
    
    def __init__(self, workflow_dir: str = "activbot/workflows",
                 schema_path: str = "activbot/schemas/workflow_schema.json"):
        self.workflow_dir = Path(workflow_dir)
        self.schema_path = Path(schema_path)
        self.schema = None
        
        if self.schema_path.exists():
            with open(self.schema_path, 'r') as f:
                self.schema = json.load(f)
                
    def validate_workflow(self, workflow_path: str) -> Tuple[bool, List[str]]:
        """
        Validate a single workflow file.
        
        Args:
            workflow_path: Path to workflow YAML file
            
        Returns:
            Tuple of (is_valid, list of errors)
        """
        errors = []
        path = Path(workflow_path)
        
        if not path.exists():
            return False, [f"Workflow file not found: {workflow_path}"]
            
        try:
            with open(path, 'r') as f:
                workflow = yaml.safe_load(f)
                
            # Schema validation
            if self.schema:
                try:
                    validate(instance=workflow, schema=self.schema)
                except ValidationError as e:
                    errors.append(f"Schema validation failed: {e.message}")
                    
            # Basic structure validation
            if not isinstance(workflow, dict):
                errors.append("Workflow must be a dictionary")
                return False, errors
                
            if 'name' not in workflow:
                errors.append("Missing required field: 'name'")
                
            if 'tasks' not in workflow:
                errors.append("Missing required field: 'tasks'")
            elif not isinstance(workflow['tasks'], list):
                errors.append("'tasks' must be a list")
            elif len(workflow['tasks']) == 0:
                errors.append("'tasks' cannot be empty")
                
            # Validate task dependencies
            if 'tasks' in workflow and isinstance(workflow['tasks'], list):
                task_names = {task.get('name') for task in workflow['tasks'] if 'name' in task}
                
                for task in workflow['tasks']:
                    if 'depends_on' in task:
                        for dep in task['depends_on']:
                            if dep not in task_names:
                                errors.append(f"Task '{task.get('name')}' depends on unknown task '{dep}'")
                                
        except yaml.YAMLError as e:
            errors.append(f"YAML parsing error: {e}")
        except Exception as e:
            errors.append(f"Unexpected error: {e}")
            
        return len(errors) == 0, errors
        
    def validate_all_workflows(self) -> dict:
        """
        Validate all workflows in the workflow directory.
        
        Returns:
            Dictionary mapping workflow names to validation results
        """
        results = {}
        
        if not self.workflow_dir.exists():
            return results
            
        for workflow_file in self.workflow_dir.glob("*.yml"):
            is_valid, errors = self.validate_workflow(str(workflow_file))
            results[workflow_file.name] = {
                'valid': is_valid,
                'errors': errors
            }
            
        return results
        
    def check_compatibility(self) -> dict:
        """
        Check if workflows are compatible with available plugins.
        
        Returns:
            Compatibility report
        """
        from .plugin_loader import PluginLoader
        
        plugin_loader = PluginLoader()
        available_plugins = plugin_loader.load_all_plugins()
        plugin_types = set(available_plugins.keys())
        
        compatibility_report = {}
        
        for workflow_file in self.workflow_dir.glob("*.yml"):
            with open(workflow_file, 'r') as f:
                workflow = yaml.safe_load(f)
                
            missing_plugins = set()
            
            for task in workflow.get('tasks', []):
                task_type = task.get('type')
                if task_type and task_type not in plugin_types:
                    missing_plugins.add(task_type)
                    
            compatibility_report[workflow_file.name] = {
                'compatible': len(missing_plugins) == 0,
                'missing_plugins': list(missing_plugins)
            }
            
        return compatibility_report


def main():
    """Command-line interface for workflow validation."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Activbot workflows')
    parser.add_argument('--validate-all', action='store_true',
                       help='Validate all workflows')
    parser.add_argument('--check-compatibility', action='store_true',
                       help='Check workflow compatibility with plugins')
    parser.add_argument('--workflow', type=str,
                       help='Validate a specific workflow file')
    
    args = parser.parse_args()
    
    validator = WorkflowValidator()
    
    if args.validate_all:
        print("Validating all workflows...")
        results = validator.validate_all_workflows()
        
        all_valid = True
        for name, result in results.items():
            status = "✓ VALID" if result['valid'] else "✗ INVALID"
            print(f"{status}: {name}")
            
            if not result['valid']:
                all_valid = False
                for error in result['errors']:
                    print(f"  - {error}")
                    
        sys.exit(0 if all_valid else 1)
        
    elif args.check_compatibility:
        print("Checking workflow compatibility...")
        report = validator.check_compatibility()
        
        all_compatible = True
        for name, result in report.items():
            status = "✓ COMPATIBLE" if result['compatible'] else "✗ INCOMPATIBLE"
            print(f"{status}: {name}")
            
            if not result['compatible']:
                all_compatible = False
                print(f"  Missing plugins: {', '.join(result['missing_plugins'])}")
                
        sys.exit(0 if all_compatible else 1)
        
    elif args.workflow:
        print(f"Validating workflow: {args.workflow}")
        is_valid, errors = validator.validate_workflow(args.workflow)
        
        if is_valid:
            print("✓ Workflow is valid")
            sys.exit(0)
        else:
            print("✗ Workflow is invalid:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
            
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
