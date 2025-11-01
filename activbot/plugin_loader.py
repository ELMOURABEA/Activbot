"""
Plugin Loader - Manages dynamic loading and updates of plugins/agents
"""
import importlib
import importlib.util
import sys
from typing import Dict, List, Any, Optional
from pathlib import Path
import inspect


class PluginLoader:
    """
    Dynamically loads and manages plugins for modular agent/task execution.
    Enables self-evolution through plugin updates without manual intervention.
    """
    
    def __init__(self, plugin_dir: str = "activbot/plugins"):
        self.plugin_dir = Path(plugin_dir)
        self.plugin_dir.mkdir(parents=True, exist_ok=True)
        self.plugins: Dict[str, Any] = {}
        self.plugin_metadata: Dict[str, Dict] = {}
        
    def load_plugin(self, plugin_name: str, plugin_path: Optional[str] = None) -> Any:
        """
        Load a plugin from a Python file.
        
        Args:
            plugin_name: Name of the plugin
            plugin_path: Optional path to plugin file (defaults to plugin_dir)
            
        Returns:
            Loaded plugin instance
        """
        if plugin_path is None:
            plugin_path = self.plugin_dir / f"{plugin_name}.py"
        else:
            plugin_path = Path(plugin_path)
            
        if not plugin_path.exists():
            raise FileNotFoundError(f"Plugin file not found: {plugin_path}")
            
        # Load the module
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load plugin: {plugin_name}")
            
        module = importlib.util.module_from_spec(spec)
        sys.modules[plugin_name] = module
        spec.loader.exec_module(module)
        
        # Find the plugin class (looks for classes with 'Plugin' in name or 'execute' method)
        # Prioritize classes with 'Plugin' in name for faster discovery
        plugin_class = None
        classes_with_execute = []
        
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if 'Plugin' in name:
                plugin_class = obj
                break
            elif hasattr(obj, 'execute'):
                classes_with_execute.append(obj)
        
        # Fallback to first class with execute method
        if plugin_class is None and classes_with_execute:
            plugin_class = classes_with_execute[0]
                
        if plugin_class is None:
            raise ValueError(f"No valid plugin class found in {plugin_path}")
            
        # Instantiate the plugin
        plugin_instance = plugin_class()
        
        # Store plugin and metadata
        self.plugins[plugin_name] = plugin_instance
        self.plugin_metadata[plugin_name] = {
            'path': str(plugin_path),
            'class_name': plugin_class.__name__,
            'module': module.__name__
        }
        
        return plugin_instance
        
    def load_all_plugins(self) -> Dict[str, Any]:
        """
        Load all plugins from the plugin directory.
        
        Returns:
            Dict mapping plugin names to instances
        """
        loaded = {}
        for plugin_file in self.plugin_dir.glob("*.py"):
            if plugin_file.name.startswith("__"):
                continue
                
            plugin_name = plugin_file.stem
            try:
                plugin = self.load_plugin(plugin_name)
                loaded[plugin_name] = plugin
            except Exception as e:
                print(f"Warning: Failed to load plugin {plugin_name}: {e}")
                
        return loaded
        
    def reload_plugin(self, plugin_name: str) -> Any:
        """
        Reload a plugin to pick up changes (for hot-reloading).
        
        Args:
            plugin_name: Name of plugin to reload
            
        Returns:
            Reloaded plugin instance
        """
        if plugin_name in self.plugins:
            # Remove from cache
            del self.plugins[plugin_name]
            if plugin_name in sys.modules:
                del sys.modules[plugin_name]
                
        # Reload the plugin
        return self.load_plugin(plugin_name)
        
    def get_plugin(self, plugin_name: str) -> Optional[Any]:
        """
        Get a loaded plugin by name.
        
        Args:
            plugin_name: Name of the plugin
            
        Returns:
            Plugin instance or None
        """
        return self.plugins.get(plugin_name)
        
    def list_plugins(self) -> List[str]:
        """
        List all loaded plugins.
        
        Returns:
            List of plugin names
        """
        return list(self.plugins.keys())
        
    def get_plugin_info(self, plugin_name: str) -> Optional[Dict]:
        """
        Get metadata about a plugin.
        
        Args:
            plugin_name: Name of the plugin
            
        Returns:
            Plugin metadata dictionary
        """
        return self.plugin_metadata.get(plugin_name)
        
    def unload_plugin(self, plugin_name: str):
        """
        Unload a plugin from memory.
        
        Args:
            plugin_name: Name of plugin to unload
        """
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            
        if plugin_name in self.plugin_metadata:
            del self.plugin_metadata[plugin_name]
            
        if plugin_name in sys.modules:
            del sys.modules[plugin_name]
