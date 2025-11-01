# Activbot

**Activbot** is a self-evolving workflow automation framework that enables dynamic workflow generation, modification, and updates without manual interventi

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

##

## Architecture

Activbot consists of several key components:

- **WorkflowEngine** - Core execution engine for processing workflows
- **WorkflowManager** - Manages workflow lifecycle and auto-generation
- **PluginLoader** - Dynamic plugin loading with hot-reload support
- **Validator** - Schema validation and compatibility checking
- **Auto-Updater** - Analyzes and suggests workflow improvements

See [WORKFLOW_ARCHITECTURE.md] for detailed documentation.

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
        self.version = "1.0
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

## UAE Commemorative Coin Project

This repository includes a QR code generation system for the UAE Commemorative Coin Project. The system generates QR codes linking to emirate-specific pages, cultural content, and project resources.

### Quick Access QR Codes

<table>
  <tr>
    <td align="center">
      <img src="uae_coin_project/qr_codes/emirate1_abudhabi_qr.png" width="120"><br>
      <b>Abu Dhabi</b>
    </td>
    <td align="center">
      <img src="uae_coin_project/qr_codes/emirate2_dubai_qr.png" width="120"><br>
      <b>Dubai</b>
    </td>
    <td align="center">
      <img src="uae_coin_project/qr_codes/falcon_eye_culture_qr.png" width="120"><br>
      <b>Culture</b>
    </td>
  </tr>
</table>

### Resources

- 📱 [QR Code Generator](uae_coin_project/generate_qr_codes.py)
- 📖 [UAE Coin Project Documentation](uae_coin_project/README.md)
- 🔄 [QR Update Instructions](uae_coin_project/docs/UPDATE_QR_DESTINATIONS.md)
- 📋 [Integration Examples](uae_coin_project/docs/INTEGRATION_EXAMPLES.md)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run `pytest` and `python
5. Submit a pull request

## License

MIT License - Copyright (c) 2025 ELMOURABEA

See [LICENSE] for details.

---

**Activbot** - Self-evolving workflow automation for the future 🚀
          
