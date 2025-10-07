# Activbot Quick Start Guide

Get started with Activbot workflow auto-design system in 5 minutes!

## Installation

```bash
# Clone and setup
git clone https://github.com/ELMOURABEA/Activbot.git
cd Activbot
pip install -r requirements.txt
```

## Run the Demo

```bash
python demo.py
```

This interactive demo shows all features:
- ✓ Auto-generating workflows
- ✓ Updating with version control
- ✓ Executing workflows
- ✓ Validating schemas
- ✓ Auto-analyzing for improvements

## Quick Commands

### Create a Workflow

```python
from activbot import WorkflowManager

manager = WorkflowManager()
tasks = [
    {'name': 'build', 'type': 'build'},
    {'name': 'test', 'type': 'test', 'depends_on': ['build']}
]
workflow = manager.create_workflow('my_pipeline', tasks)
```

### Auto-Generate from Requirements

```python
from activbot import WorkflowManager

manager = WorkflowManager()
requirements = {
    'name': 'auto_workflow',
    'goals': [
        {'type': 'build', 'description': 'Build project'},
        {'type': 'test', 'description': 'Run tests'}
    ]
}
workflow = manager.generate_workflow_from_requirements(requirements)
```

### Execute a Workflow

```python
from activbot import WorkflowEngine

engine = WorkflowEngine()
engine.load_workflow('activbot/workflows/simple_workflow.yml')
results = engine.execute_workflow('simple_workflow')
print(results)
```

### Validate Workflows

```bash
python -m activbot.validator --validate-all
```

### Check for Updates

```bash
python -m activbot.updater --report
```

### Run Tests

```bash
pytest tests/ -v
```

## Directory Structure

```
activbot/
├── workflows/        # Workflow definitions (YAML)
├── plugins/          # Task execution plugins
└── schemas/          # Validation schemas

tests/               # Unit tests
examples/            # Usage examples
config.yml           # Configuration
```

## Creating a Custom Plugin

```python
# Save as activbot/plugins/my_plugin.py
from activbot.plugins.base_plugin import BasePlugin

class MyPlugin(BasePlugin):
    def execute(self, task, context):
        # Your logic here
        return {
            'name': task['name'],
            'status': 'completed',
            'output': 'Task done'
        }
```

## Workflow YAML Format

```yaml
name: my_workflow
version: 1.0.0
tasks:
  - name: task1
    type: build
    description: Build the project
  - name: task2
    type: test
    description: Run tests
    depends_on: [task1]
    retry:
      max_attempts: 3
      delay: 5
```

## Next Steps

1. ✅ Run `python demo.py` to see features
2. ✅ Read [WORKFLOW_ARCHITECTURE.md](WORKFLOW_ARCHITECTURE.md) for details
3. ✅ Check [examples/README.md](examples/README.md) for more examples
4. ✅ Create your first workflow
5. ✅ Build custom plugins for your needs

## Key Features

- **Auto-Design** - Generate workflows from requirements
- **Self-Evolution** - Auto-analyze and suggest improvements
- **Modular** - Plugin-based extensible architecture
- **Validated** - JSON Schema validation built-in
- **Versioned** - Track all workflow changes
- **Tested** - Comprehensive test suite included

## Need Help?

- 📖 Full docs: [README.md](README.md)
- 🏗️ Architecture: [WORKFLOW_ARCHITECTURE.md](WORKFLOW_ARCHITECTURE.md)
- 💡 Examples: [examples/README.md](examples/README.md)
- 📝 Summary: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

---

**Ready to build self-evolving workflows?** Run `python demo.py` now! 🚀
