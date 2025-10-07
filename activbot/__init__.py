"""
Activbot - Auto-Design Workflow System
A modular, self-evolving workflow automation framework.
"""

__version__ = "0.1.0"

from .workflow_engine import WorkflowEngine
from .workflow_manager import WorkflowManager
from .plugin_loader import PluginLoader

__all__ = ["WorkflowEngine", "WorkflowManager", "PluginLoader"]
