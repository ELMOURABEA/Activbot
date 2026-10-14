# Activbot

**Activbot** is a self-evolving workflow automation framework that enables dynamic workflow generation, modification, and updates without manual intervention.

[![CI](https://github.com/ELMOURABEA/Activbot/workflows/CI/badge.svg)](https://github.com/ELMOURABEA/Activbot/actions)
[![Workflow Auto-Update System](https://github.com/ELMOURABEA/Activbot/workflows/Workflow%20Auto-Update%20System/badge.svg)](https://github.com/ELMOURABEA/Activbot/actions)

## Features

- **🔄 Auto-Design Workflows** - Dynamically generate and modify workflows based on requirements
- **🔌 Modular Plugin System** - Extensible architecture for custom task types
- **📊 Workflow Validation** - Schema-based validation and compatibility checking
- **🚀 Automated Updates** - Self-evolving system with automatic improvement suggestions
- **🧪 Comprehensive Testing** - Full test suite with CI/CD integration
- **📈 Version Control** - Track workflow changes and maintain history

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ELMOURABEA/Activbot.git
cd Activbot

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from activbot import WorkflowEngine, WorkflowManager

# Create a workflow
manager = WorkflowManager()
tasks = [
    {'name': 'build', 'type': 'build', 'description': 'Build project'},
    {'name': 'test', 'type': 'test', 'description': 'Run tests', 'depends_on': ['build']}
]
workflow = manager.create_workflow('my_workflow', tasks)

# Execute the workflow
engine = WorkflowEngine()
engine.load_workflow('activbot/workflows/my_workflow.yml')
results = engine.execute_workflow('my_workflow')
print(results)
```

### Auto-Generate Workflows

```python
from activbot import WorkflowManager

manager = WorkflowManager()

# Define requirements
requirements = {
    'name': 'ci_pipeline',
    'goals': [
        {'type': 'git', 'description': 'Checkout code'},
        {'type': 'build', 'description': 'Build application'},
        {'type': 'test', 'description': 'Run tests', 'depends_on': ['task_2_build']}
    ]
}

# Generate workflow automatically
workflow = manager.generate_workflow_from_requirements(requirements)
```

## Architecture

Activbot consists of several key components:

- **WorkflowEngine** - Core execution engine for processing workflows
- **WorkflowManager** - Manages workflow lifecycle and auto-generation
- **PluginLoader** - Dynamic plugin loading with hot-reload support
- **Validator** - Schema validation and compatibility checking
- **Auto-Updater** - Analyzes and suggests workflow improvements

See [WORKFLOW_ARCHITECTURE.md](WORKFLOW_ARCHITECTURE.md) for detailed documentation.

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=activbot --cov-report=term-missing

# Validate workflows
python -m activbot.validator --validate-all

# Check for updates
python -m activbot.updater --report
```

## Creating Custom Plugins

```python
from activbot.plugins.base_plugin import BasePlugin

class MyCustomPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        
    def execute(self, task, context):
        # Your custom logic here
        return {
            'name': task['name'],
            'status': 'completed',
            'output': 'Custom task executed'
        }
```

Save to `activbot/plugins/my_custom_plugin.py` and it will be auto-discovered.

## CI/CD Integration

Activbot includes automated workflows for:

- ✅ Workflow validation on every push
- ✅ Automated testing with pytest
- ✅ Plugin compatibility checking
- ✅ Auto-update suggestions

See `.github/workflows/workflow-auto-update.yml` for details.

## Configuration

Configure Activbot via `config.yml`:

```yaml
activbot:
  engine:
    workflow_dir: "activbot/workflows"
    plugin_dir: "activbot/plugins"
  auto_update:
    enabled: true
    check_interval: 3600
```

## Eligibility for Updates

### ✅ Modular Architecture
- Plugin-based system for easy extensibility
- Hot-reloading support for development
- Clear separation of concerns

### ✅ Automated Pipeline
- CI/CD workflow validates changes automatically
- Continuous testing ensures reliability
- Auto-update system suggests improvements

### ✅ Continuous Integration
- GitHub Actions integration
- Automated testing on every push
- Plugin and workflow compatibility checking

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run `pytest` and `python -m activbot.validator --validate-all`
5. Submit a pull request

## License

MIT License - Copyright (c) 2025 ELMOURABEA

See [LICENSE](LICENSE) for details.

---

**Activbot** - Self-evolving workflow automation for the future 🚀
          
# name: Build and push
        id: build-and-push
        uses: docker/build-push-action@v6
        with:
          context: .
          file: images/Dockerfile
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            RUNNER_VERSION=${{ env.RUNNER_VERSION }}
            RUNNER_CONTAINER_HOOKS_VERSION=${{ env.RUNNER_CONTAINER_HOOKS_VERSION }}
          load: true
          push:
            ${{ github.event_name == 'push' && github.ref == 'refs/heads/main'
            && github.repository == 'usatlas/runner' }}

      - name: Generate attestation
        # every PR will trigger a push event on main, so check the push event is actually coming from main
        if:
          github.event_name == 'push' && github.ref == 'refs/heads/main' &&
          github.repository == 'usatlas/runner'
        uses: actions/attest-build-provenance@v3
        with:
          subject-name: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          subject-digest: ${{ steps.build-and-push.outputs.digest }}
          push-to-registry: true
