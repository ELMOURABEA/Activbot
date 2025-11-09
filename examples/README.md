# Activbot Examples

This directory contains examples demonstrating the Activbot workflow auto-design system.

## Running the Demo

To see all features in action:

```bash
python demo.py
```

This will demonstrate:
1. **Auto-generating workflows** from requirements
2. **Updating workflows** with version control
3. **Executing workflows** with the engine
4. **Validating workflows** against schema
5. **Auto-analyzing** for improvements

## Example 1: Create a Simple Workflow

```python
from activbot import WorkflowManager

manager = WorkflowManager()

tasks = [
    {'name': 'setup', 'type': 'setup', 'description': 'Setup environment'},
    {'name': 'build', 'type': 'build', 'description': 'Build project', 'depends_on': ['setup']},
    {'name': 'test', 'type': 'test', 'description': 'Run tests', 'depends_on': ['build']}
]

workflow = manager.create_workflow('my_ci_pipeline', tasks)
print(f"Created workflow: {workflow['name']} v{workflow['version']}")
```

## Example 2: Auto-Generate from Requirements

```python
from activbot import WorkflowManager

manager = WorkflowManager()

requirements = {
    'name': 'automated_workflow',
    'goals': [
        {'type': 'checkout', 'description': 'Get source code'},
        {'type': 'build', 'description': 'Compile application'},
        {'type': 'test', 'description': 'Run test suite', 'depends_on': ['task_2_build']},
        {'type': 'deploy', 'description': 'Deploy app', 'depends_on': ['task_3_test']}
    ]
}

workflow = manager.generate_workflow_from_requirements(requirements)
```

## Example 3: Execute a Workflow

```python
from activbot import WorkflowEngine, PluginLoader

# Load plugins
loader = PluginLoader()
plugins = loader.load_all_plugins()

# Setup engine
engine = WorkflowEngine()
for name, plugin in plugins.items():
    engine.register_plugin(name, plugin)

# Execute
engine.load_workflow('activbot/workflows/simple_workflow.yml')
results = engine.execute_workflow('simple_workflow')

print(f"Status: {results['status']}")
for task in results['tasks']:
    print(f"  {task['name']}: {task['status']}")
```

## Example 4: Update a Workflow

```python
from activbot import WorkflowManager

manager = WorkflowManager()

updates = {
    'description': 'Updated pipeline with enhanced features',
    'tasks': [
        {'name': 'build', 'type': 'build', 'description': 'Build with caching'},
        {'name': 'test', 'type': 'test', 'description': 'Run tests', 
         'depends_on': ['build'],
         'retry': {'max_attempts': 3, 'delay': 5}}
    ]
}

updated = manager.update_workflow('my_ci_pipeline', updates, 
                                 reason='Added retry logic')
print(f"Updated to v{updated['version']}")
```

## Example 5: Validate Workflows

```bash
# Validate all workflows
python -m activbot.validator --validate-all

# Check compatibility with plugins
python -m activbot.validator --check-compatibility

# Validate specific workflow
python -m activbot.validator --workflow activbot/workflows/simple_workflow.yml
```

## Example 6: Analyze for Improvements

```bash
# Check plugin updates
python -m activbot.updater --check-plugins

# Analyze workflows
python -m activbot.updater --analyze-workflows

# Generate full report
python -m activbot.updater --report
```

## Example 7: Create a Custom Plugin

```python
# Save as activbot/plugins/my_plugin.py
from activbot.plugins.base_plugin import BasePlugin

class MyCustomPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        
    def execute(self, task, context):
        task_name = task.get('name')
        params = task.get('parameters', {})
        
        # Your custom logic here
        print(f"Executing {task_name} with {params}")
        
        return {
            'name': task_name,
            'type': task.get('type'),
            'status': 'completed',
            'output': f'{task_name} completed successfully'
        }
```

Then use it in a workflow:

```yaml
name: custom_workflow
version: 1.0.0
tasks:
  - name: my_task
    type: my_custom
    parameters:
      key: value
```

## Example 8: Workflow with Dependencies

```yaml
name: complex_pipeline
version: 1.0.0
description: Workflow with complex task dependencies
tasks:
  - name: checkout
    type: git
    description: Checkout code
    
  - name: build_frontend
    type: build
    description: Build frontend
    depends_on: [checkout]
    
  - name: build_backend
    type: build
    description: Build backend
    depends_on: [checkout]
    
  - name: test_integration
    type: test
    description: Integration tests
    depends_on: [build_frontend, build_backend]
    retry:
      max_attempts: 3
      delay: 5
      
  - name: deploy
    type: deploy
    description: Deploy to production
    depends_on: [test_integration]
    parameters:
      environment: production
```

## Workflow Schema

All workflows must follow this structure:

```yaml
name: workflow_name           # Required: Unique identifier
version: 1.0.0               # Semantic version
description: Description     # Optional: Human-readable description
created_at: 2025-01-01T00:00:00  # ISO 8601 timestamp
metadata:                    # Optional metadata
  auto_generated: false
  tags: [ci, testing]
tasks:                       # Required: List of tasks
  - name: task_name          # Required
    type: task_type          # Required
    description: Task description
    parameters:              # Task-specific parameters
      key: value
    depends_on:              # List of task dependencies
      - previous_task
    retry:                   # Optional retry configuration
      max_attempts: 3
      delay: 5
```

## Additional Resources

- [WORKFLOW_ARCHITECTURE.md](../WORKFLOW_ARCHITECTURE.md) - Complete architecture documentation
- [config.yml](../config.yml) - System configuration options
- [Workflow Schema](../activbot/schemas/workflow_schema.json) - JSON schema for validation

## Testing Your Workflows

Run the test suite:

```bash
# All tests
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=activbot --cov-report=html

# Specific test file
pytest tests/test_workflow_engine.py -v
```

## Tips for Success

1. **Start Simple** - Begin with basic workflows and gradually add complexity
2. **Use Validation** - Always validate workflows before execution
3. **Version Control** - Track workflow changes with semantic versioning
4. **Add Retry Logic** - Use retry configuration for critical tasks
5. **Leverage Auto-Generation** - Let the system create workflows from requirements
6. **Monitor Analysis** - Check auto-update reports regularly for improvements

## Need Help?

- Check the [main README](../README.md)
- Review [architecture docs](../WORKFLOW_ARCHITECTURE.md)
- Run the demo: `python demo.py`
- Examine example workflows in `activbot/workflows/`
