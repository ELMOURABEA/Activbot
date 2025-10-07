"""
Tests for PluginLoader
"""
import pytest
import tempfile
import shutil
from pathlib import Path
from activbot.plugin_loader import PluginLoader


class TestPluginLoader:
    """Test cases for PluginLoader"""
    
    @pytest.fixture
    def temp_plugin_dir(self):
        """Create a temporary directory for plugins"""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)
        
    @pytest.fixture
    def sample_plugin(self, temp_plugin_dir):
        """Create a sample plugin file"""
        plugin_code = '''
class TestPlugin:
    """Test plugin for unit tests"""
    
    def __init__(self):
        self.name = "TestPlugin"
        
    def execute(self, task, context):
        return {"status": "completed", "output": "Test executed"}
'''
        plugin_path = Path(temp_plugin_dir) / "test_plugin.py"
        plugin_path.write_text(plugin_code)
        return plugin_path
        
    def test_loader_initialization(self, temp_plugin_dir):
        """Test loader can be initialized"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        assert loader is not None
        assert loader.plugin_dir.exists()
        
    def test_load_plugin(self, temp_plugin_dir, sample_plugin):
        """Test loading a single plugin"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        plugin = loader.load_plugin('test_plugin')
        
        assert plugin is not None
        assert 'test_plugin' in loader.plugins
        assert hasattr(plugin, 'execute')
        
    def test_load_nonexistent_plugin(self, temp_plugin_dir):
        """Test loading a nonexistent plugin raises error"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        with pytest.raises(FileNotFoundError):
            loader.load_plugin('nonexistent_plugin')
            
    def test_get_plugin(self, temp_plugin_dir, sample_plugin):
        """Test getting a loaded plugin"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        loader.load_plugin('test_plugin')
        plugin = loader.get_plugin('test_plugin')
        
        assert plugin is not None
        
    def test_get_nonexistent_plugin(self, temp_plugin_dir):
        """Test getting a nonexistent plugin returns None"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        plugin = loader.get_plugin('nonexistent')
        assert plugin is None
        
    def test_list_plugins(self, temp_plugin_dir, sample_plugin):
        """Test listing loaded plugins"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        assert loader.list_plugins() == []
        
        loader.load_plugin('test_plugin')
        plugins = loader.list_plugins()
        
        assert len(plugins) == 1
        assert 'test_plugin' in plugins
        
    def test_unload_plugin(self, temp_plugin_dir, sample_plugin):
        """Test unloading a plugin"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        loader.load_plugin('test_plugin')
        assert 'test_plugin' in loader.plugins
        
        loader.unload_plugin('test_plugin')
        assert 'test_plugin' not in loader.plugins
        
    def test_get_plugin_info(self, temp_plugin_dir, sample_plugin):
        """Test getting plugin metadata"""
        loader = PluginLoader(plugin_dir=temp_plugin_dir)
        
        loader.load_plugin('test_plugin')
        info = loader.get_plugin_info('test_plugin')
        
        assert info is not None
        assert 'path' in info
        assert 'class_name' in info
        assert info['class_name'] == 'TestPlugin'
