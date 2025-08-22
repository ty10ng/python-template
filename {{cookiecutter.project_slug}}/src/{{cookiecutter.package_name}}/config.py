"""
Configuration management module for viren.

This module handles hierarchical configuration loading:
DEFAULTS < CONFIG_FILE < Environment Variables

Environment variables take precedence over config file, which takes precedence over defaults.
"""

import os
import yaml
from pathlib import Path
from typing import Any, Dict, Optional, Union
from .logger import get_logger

# Initialize logger for this module
logger = get_logger(__name__)


class VirenConfig:
    """Hierarchical configuration manager for viren."""
    
    # Default configuration values
    DEFAULT_CONFIG = {
        'logging': {
            'level': 'INFO',
            'console_level': 'INFO',
            'file_level': 'DEBUG',
            'file_path': 'logs/viren.log',
            'max_file_size': '10MB',
            'backup_count': 5
        },
        'api': {
            'timeout': 30,
            'max_retries': 3,
            'base_url': None
        },
        'database': {
            'url': None,
            'pool_size': 5,
            'max_overflow': 10,
            'pool_timeout': 30
        },
        'app': {
            'name': 'viren',
            'version': '1.0.0',
            'debug': False
        }
    }
    
    def __init__(self, config_file_env_var: str = 'VIREN_CONFIG_FILE'):
        """
        Initialize the configuration manager.
        
        Args:
            config_file_env_var: Environment variable name that contains the config file path
        """
        self.config_file_env_var = config_file_env_var
        self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")
        self._config = {}
        self._load_configuration()
    
    def _load_configuration(self):
        """Load configuration from defaults, config file, and environment variables."""
        self.logger.info("Loading configuration hierarchy...")
        
        # Start with defaults
        self._config = self._deep_copy_dict(self.DEFAULT_CONFIG)
        self.logger.debug("✅ Loaded default configuration")
        
        # Load from config file if specified
        config_file_path = os.getenv(self.config_file_env_var)
        if config_file_path:
            self._load_config_file(config_file_path)
        else:
            self.logger.debug(f"ℹ️  No config file specified in {self.config_file_env_var}")
        
        # Override with environment variables
        self._load_environment_overrides()
        
        self.logger.info("Configuration loading complete")
    
    def _load_config_file(self, config_file_path: str):
        """Load configuration from YAML file."""
        try:
            config_path = Path(config_file_path)
            
            if not config_path.exists():
                self.logger.warning(f"⚠️  Config file not found: {config_file_path}")
                return
            
            if not config_path.is_file():
                self.logger.warning(f"⚠️  Config path is not a file: {config_file_path}")
                return
            
            with open(config_path, 'r', encoding='utf-8') as f:
                file_config = yaml.safe_load(f)
            
            if file_config is None:
                self.logger.warning(f"⚠️  Config file is empty: {config_file_path}")
                return
            
            if not isinstance(file_config, dict):
                self.logger.error(f"❌ Config file must contain a YAML dictionary: {config_file_path}")
                return
            
            # Merge file config into current config
            self._deep_merge_dict(self._config, file_config)
            self.logger.info(f"✅ Loaded config file: {config_file_path}")
            
        except yaml.YAMLError as e:
            self.logger.error(f"❌ Error parsing YAML config file {config_file_path}: {e}")
        except Exception as e:
            self.logger.error(f"❌ Error loading config file {config_file_path}: {e}")
    
    def _load_environment_overrides(self):
        """Load environment variable overrides using a mapping system."""
        # Define environment variable mappings to config paths
        env_mappings = {
            # Logging configuration
            'VIREN_LOG_LEVEL': 'logging.level',
            'VIREN_CONSOLE_LOG_LEVEL': 'logging.console_level', 
            'VIREN_FILE_LOG_LEVEL': 'logging.file_level',
            'VIREN_LOG_FILE_PATH': 'logging.file_path',
            'VIREN_LOG_MAX_FILE_SIZE': 'logging.max_file_size',
            'VIREN_LOG_BACKUP_COUNT': 'logging.backup_count',
            
            # API configuration
            'API_TIMEOUT': 'api.timeout',
            'MAX_RETRIES': 'api.max_retries',
            'API_BASE_URL': 'api.base_url',
            
            # Database configuration
            'DATABASE_URL': 'database.url',
            'DB_POOL_SIZE': 'database.pool_size',
            'DB_MAX_OVERFLOW': 'database.max_overflow',
            'DB_POOL_TIMEOUT': 'database.pool_timeout',
            
            # App configuration
            'VIREN_APP_NAME': 'app.name',
            'VIREN_APP_VERSION': 'app.version',
            'VIREN_DEBUG': 'app.debug'
        }
        
        override_count = 0
        for env_var, config_path in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                # Convert string values to appropriate types
                converted_value = self._convert_env_value(env_value, config_path)
                self._set_nested_value(self._config, config_path, converted_value)
                self.logger.debug(f"✅ Environment override: {env_var} -> {config_path} = {converted_value}")
                override_count += 1
        
        if override_count > 0:
            self.logger.info(f"✅ Applied {override_count} environment variable override(s)")
        else:
            self.logger.debug("ℹ️  No environment variable overrides found")
    
    def _convert_env_value(self, value: str, config_path: str) -> Any:
        """Convert environment variable string to appropriate type based on config path."""
        # Handle boolean values
        if config_path.endswith('.debug') or 'debug' in config_path.lower():
            return value.lower() in ('true', '1', 'yes', 'on')
        
        # Handle integer values
        if any(key in config_path for key in ['timeout', 'retries', 'pool_size', 'overflow', 'count']):
            try:
                return int(value)
            except ValueError:
                self.logger.warning(f"⚠️  Could not convert '{value}' to integer for {config_path}, using string")
                return value
        
        # Handle float values for file sizes
        if 'file_size' in config_path:
            try:
                # Handle sizes like "10MB", "1GB", etc.
                if value.upper().endswith('MB'):
                    return float(value[:-2]) * 1024 * 1024
                elif value.upper().endswith('GB'):
                    return float(value[:-2]) * 1024 * 1024 * 1024
                elif value.upper().endswith('KB'):
                    return float(value[:-2]) * 1024
                else:
                    return float(value)
            except ValueError:
                self.logger.warning(f"⚠️  Could not convert '{value}' to file size for {config_path}, using string")
                return value
        
        # Default to string
        return value
    
    def _set_nested_value(self, config_dict: Dict, path: str, value: Any):
        """Set a nested dictionary value using dot notation path."""
        keys = path.split('.')
        current = config_dict
        
        # Navigate to the parent of the target key
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # Set the final value
        current[keys[-1]] = value
    
    def _deep_copy_dict(self, source: Dict) -> Dict:
        """Create a deep copy of a dictionary."""
        result = {}
        for key, value in source.items():
            if isinstance(value, dict):
                result[key] = self._deep_copy_dict(value)
            else:
                result[key] = value
        return result
    
    def _deep_merge_dict(self, target: Dict, source: Dict):
        """Deep merge source dictionary into target dictionary."""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._deep_merge_dict(target[key], value)
            else:
                target[key] = value
    
    def get(self, path: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation.
        
        Args:
            path: Dot-separated path to the config value (e.g., 'logging.level')
            default: Default value if path not found
            
        Returns:
            Configuration value or default
        """
        keys = path.split('.')
        current = self._config
        
        try:
            for key in keys:
                current = current[key]
            return current
        except (KeyError, TypeError):
            return default
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """
        Get an entire configuration section.
        
        Args:
            section: Section name (e.g., 'logging', 'api')
            
        Returns:
            Dictionary containing the section configuration
        """
        return self._config.get(section, {})
    
    def get_all(self) -> Dict[str, Any]:
        """Get the entire configuration dictionary."""
        return self._deep_copy_dict(self._config)
    
    def reload(self):
        """Reload configuration from all sources."""
        self.logger.info("Reloading configuration...")
        self._load_configuration()
    
    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access to config sections."""
        return self._config[key]
    
    def __contains__(self, key: str) -> bool:
        """Check if a configuration section exists."""
        return key in self._config


# Global configuration instance
_config_instance: Optional[VirenConfig] = None


def get_config() -> VirenConfig:
    """
    Get the global configuration instance.
    
    Returns:
        VirenConfig: The global configuration instance
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = VirenConfig()
    return _config_instance


def reload_config():
    """Reload the global configuration instance."""
    global _config_instance
    if _config_instance is not None:
        _config_instance.reload()
    else:
        _config_instance = VirenConfig()
