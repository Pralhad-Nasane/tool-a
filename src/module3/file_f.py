"""
Demonstrates inheritance examples with proper docstrings and class hierarchy.
"""


class BaseTool:
    """
    Base class for all tool implementations.
    
    This is the parent class that defines the interface for all tools
    in the system. Subclasses should override the run() method to provide
    specific functionality.
    
    Attributes:
        name (str): The name of the tool.
        version (str): The version of the tool.
        enabled (bool): Whether the tool is enabled or disabled.
    """
    
    def __init__(self, name, version="1.0", enabled=True):
        """
        Initialize the BaseTool.
        
        Args:
            name (str): The name of the tool.
            version (str, optional): The version of the tool. Defaults to "1.0".
            enabled (bool, optional): Whether the tool is enabled. Defaults to True.
        """
        self.name = name
        self.version = version
        self.enabled = enabled
    
    def run(self):
        """
        Execute the tool's main functionality.
        
        This method should be overridden by subclasses to provide
        specific implementation details.
        
        Returns:
            str: A message describing the execution result.
        """
        print(f"Running base tool: {self.name}")
        return f"Base tool {self.name} executed."
    
    def get_info(self):
        """
        Retrieve information about the tool.
        
        Returns:
            dict: A dictionary containing tool metadata.
        """
        return {
            "name": self.name,
            "version": self.version,
            "enabled": self.enabled
        }


class CustomTool(BaseTool):
    """
    Custom tool implementation that extends BaseTool.
    
    This class inherits from BaseTool and provides custom functionality
    while maintaining the same interface.
    
    Attributes:
        name (str): The name of the tool.
        version (str): The version of the tool.
        enabled (bool): Whether the tool is enabled.
        custom_config (dict): Custom configuration for this tool.
    """
    
    def __init__(self, name, version="1.0", enabled=True, custom_config=None):
        """
        Initialize the CustomTool.
        
        Args:
            name (str): The name of the tool.
            version (str, optional): The version of the tool. Defaults to "1.0".
            enabled (bool, optional): Whether the tool is enabled. Defaults to True.
            custom_config (dict, optional): Custom configuration dictionary. Defaults to None.
        """
        super().__init__(name, version, enabled)
        self.custom_config = custom_config or {}
    
    def run(self):
        """
        Execute the custom tool with enhanced functionality.
        
        Returns:
            str: A message describing the custom execution result.
        """
        print(f"Running custom tool: {self.name}")
        return f"Custom tool {self.name} executed with config: {self.custom_config}"


class AdvancedTool(BaseTool):
    """
    Advanced tool with additional features and logging capabilities.
    
    This class extends BaseTool with advanced features such as
    logging, error handling, and performance monitoring.
    
    Attributes:
        name (str): The name of the tool.
        version (str): The version of the tool.
        enabled (bool): Whether the tool is enabled.
        log_file (str): Path to the log file.
        timeout (int): Maximum execution time in seconds.
    """
    
    def __init__(self, name, version="2.0", enabled=True, log_file=None, timeout=30):
        """
        Initialize the AdvancedTool.
        
        Args:
            name (str): The name of the tool.
            version (str, optional): The version of the tool. Defaults to "2.0".
            enabled (bool, optional): Whether the tool is enabled. Defaults to True.
            log_file (str, optional): Path to store logs. Defaults to None.
            timeout (int, optional): Maximum execution time in seconds. Defaults to 30.
        """
        super().__init__(name, version, enabled)
        self.log_file = log_file
        self.timeout = timeout
        self.execution_count = 0
    
    def run(self):
        """
        Execute the advanced tool with logging and monitoring.
        
        Returns:
            dict: A dictionary containing execution results and metadata.
        """
        self.execution_count += 1
        print(f"Running advanced tool: {self.name}")
        return {
            "status": "success",
            "tool_name": self.name,
            "execution_count": self.execution_count,
            "timeout": self.timeout
        }
    
    def get_stats(self):
        """
        Get execution statistics for the tool.
        
        Returns:
            dict: Dictionary containing execution statistics.
        """
        return {
            "name": self.name,
            "execution_count": self.execution_count,
            "timeout": self.timeout
        }


class PluginTool(AdvancedTool):
    """
    Plugin-based tool that extends AdvancedTool with plugin capabilities.
    
    This class adds support for loading and managing plugins,
    extending the functionality of the advanced tool.
    
    Attributes:
        name (str): The name of the tool.
        version (str): The version of the tool.
        enabled (bool): Whether the tool is enabled.
        log_file (str): Path to the log file.
        timeout (int): Maximum execution time in seconds.
        plugins (list): List of loaded plugins.
    """
    
    def __init__(self, name, version="3.0", enabled=True, log_file=None, timeout=30, plugins=None):
        """
        Initialize the PluginTool.
        
        Args:
            name (str): The name of the tool.
            version (str, optional): The version of the tool. Defaults to "3.0".
            enabled (bool, optional): Whether the tool is enabled. Defaults to True.
            log_file (str, optional): Path to store logs. Defaults to None.
            timeout (int, optional): Maximum execution time in seconds. Defaults to 30.
            plugins (list, optional): List of plugins to load. Defaults to None.
        """
        super().__init__(name, version, enabled, log_file, timeout)
        self.plugins = plugins or []
    
    def add_plugin(self, plugin_name):
        """
        Add a plugin to the tool.
        
        Args:
            plugin_name (str): The name of the plugin to add.
            
        Returns:
            bool: True if plugin was added successfully, False otherwise.
        """
        if plugin_name not in self.plugins:
            self.plugins.append(plugin_name)
            return True
        return False
    
    def run(self):
        """
        Execute the plugin tool with all loaded plugins.
        
        Returns:
            dict: Dictionary containing execution results and plugin information.
        """
        base_result = super().run()
        base_result["plugins"] = self.plugins
        base_result["plugin_count"] = len(self.plugins)
        return base_result
