# Activbot Workflow Auto-Design Architecture

## Overview

Activbot is a self-evolving workflow automation framework that enables dynamic workflow generation, modification, and updates without manual intervention. The system provides a modular architecture for plugin/agent updates and automated pipelines for continuous workflow improvement.

## Architecture Components

### 1. Workflow Engine (`activbot/workflow_engine.py`)

The core execution engine that processes workflow definitions and executes tasks dynamically.

**Key Features:**
- Load workflows from YAML files
- Execute tasks sequentially or with dependencies
- Plugin-based task execution
- Context sharing between tasks

**Usage:**
```python
from activbot import WorkflowEngine

engine = WorkflowEngine()
engine.load_workflow('activbot/workflows/example_ci_workflow.yml')
results = engine.execute_workflow('example_ci_workflow')
```

### 2. Workflow Manager (`activbot/workflow_manager.py`)

Manages workflow lifecycle including creation, updates, and versioning. Enables auto-design and self-evolution.

**Key Features:**
- Dynamic workflow creation
- Version-controlled updates
- Auto-generation from requirements
- Workflow validation
- History tracking

**Usage:**
```python
from activbot import WorkflowManager

manager = WorkflowManager()

# Create a new workflow
tasks = [
    {'name': 'build', 'type': 'build'},
    {'name': 'test', 'type': 'test', 'depends_on': ['build']}
]
workflow = manager.create_workflow('my_workflow', tasks)

# Auto-generate from requirements
requirements = {
    'name': 'auto_workflow',
    'goals': [
        {'type': 'build', 'description': 'Build project'},
        {'type': 'test', 'description': 'Run tests'}
    ]
}
workflow = manager.generate_workflow_from_requirements(requirements)
```

### 3. Plugin Loader (`activbot/plugin_loader.py`)

Dynamically loads and manages plugins for modular agent/task execution. Enables self-evolution through plugin updates.

**Key Features:**
- Dynamic plugin loading
- Hot-reloading support
- Plugin metadata management
- Automatic discovery and loading

**Usage:**
```python
from activbot import PluginLoader

loader = PluginLoader()

# Load all plugins
plugins = loader.load_all_plugins()

# Load specific plugin
plugin = loader.load_plugin('example_plugin')

# Reload plugin for updates
plugin = loader.reload_plugin('example_plugin')
```

### 4. Workflow Validator (`activbot/validator.py`)

Validates workflow definitions against schema and checks compatibility with available plugins.

**Key Features:**
- JSON Schema validation
- Task dependency validation
- Plugin compatibility checking
- Command-line interface

**Usage:**
```bash
# Validate all workflows
python -m activbot.validator --validate-all

# Check compatibility
python -m activbot.validator --check-compatibility

# Validate specific workflow
python -m activbot.validator --workflow path/to/workflow.yml
```

### 5. Auto-Updater (`activbot/updater.py`)

Automatically analyzes and suggests improvements to workflows. Enables self-evolution of the workflow system.

**Key Features:**
- Plugin update checking
- Workflow analysis and optimization suggestions
- Auto-update reports
- Safe update application

**Usage:**
```bash
# Check plugin updates
python -m activbot.updater --check-plugins

# Analyze workflows
python -m activbot.updater --analyze-workflows

# Generate report
python -m activbot.updater --report
```

## Workflow Definition Format

Workflows are defined in YAML format following this structure:

```yaml
name: workflow_name
version: 1.0.0
description: Workflow description
created_at: '2025-01-01T00:00:00'
metadata:
  auto_generated: false
  tags:
    - ci
    - testing
tasks:
  - name: task1
    type: build
    description: Build the project
    parameters:
      output_dir: dist/
  - name: task2
    type: test
    description: Run tests
    depends_on:
      - task1
    retry:
      max_attempts: 3
      delay: 5
```

## Plugin Development

Create custom plugins by extending the `BasePlugin` class:

```python
from activbot.plugins.base_plugin import BasePlugin

class MyPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        
    def execute(self, task, context):
        # Your task execution logic
        task_name = task.get('name')
        parameters = task.get('parameters', {})
        
        # Perform work
        result = {
            'name': task_name,
            'type': task.get('type'),
            'status': 'completed',
            'output': 'Task completed successfully'
        }
        
        return result
```

Save the plugin in `activbot/plugins/my_plugin.py` and it will be automatically discovered.

## CI/CD Integration

The system includes automated CI/CD workflows:

### Workflow Auto-Update System (`.github/workflows/workflow-auto-update.yml`)

Automatically validates workflows and checks for updates on every push:

1. **Validate Workflows** - Ensures all workflow definitions are valid
2. **Test Workflow Engine** - Runs comprehensive tests
3. **Auto-Update Check** - Analyzes for potential improvements

## Eligibility Criteria

### ✅ Modular Architecture
- Plugin-based system allows easy addition of new task types
- Hot-reloading support for development
- Clear separation of concerns (Engine, Manager, Loader)

### ✅ Automated Pipeline
- CI/CD workflow validates changes automatically
- Continuous testing ensures reliability
- Auto-update system suggests improvements

### ✅ Continuous Integration
- GitHub Actions integration
- Automated testing on every push
- Plugin and workflow compatibility checking

## Future Enhancements

1. **AI-Powered Workflow Generation**
   - Use ML models to suggest optimal workflows
   - Learn from execution patterns

2. **Advanced Dependency Resolution**
   - Parallel task execution
   - Dynamic resource allocation

3. **Distributed Execution**
   - Multi-node workflow execution
   - Cloud-native deployment

4. **Visual Workflow Designer**
   - Web-based UI for workflow creation
   - Real-time validation and testing

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create your first workflow:
   ```python
   from activbot import WorkflowManager
   
   manager = WorkflowManager()
   tasks = [{'name': 'hello', 'type': 'example'}]
   workflow = manager.create_workflow('hello_world', tasks)
   ```

3. Execute the workflow:
   ```python
   from activbot import WorkflowEngine
   
   engine = WorkflowEngine()
   engine.load_workflow('activbot/workflows/hello_world.yml')
   results = engine.execute_workflow('hello_world')
   print(results)
   ```

4. Run tests:
   ```bash
   pytest tests/ -v
   ```

## Contributing

When adding new features:
1. Create plugins for new task types
2. Update workflow schemas if needed
3. Add tests for new functionality
4. Update documentation
5. Run validation: `python -m activbot.validator --validate-all`

## License

MIT License - See LICENSE file for details
