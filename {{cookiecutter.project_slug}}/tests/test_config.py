"""
Tests for the configuration module.
"""

import pytest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch, mock_open

# Note: Import will be dynamically resolved when template is rendered
# from {{cookiecutter.package_name}}.config import Config, get_config


class TestConfig:
    """Test cases for the Config class."""
    
    def test_config_initialization(self):
        """Test that Config initializes with defaults."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        config = Config()
        assert config is not None
        # Should have some default values
        assert config.get('logging.level') is not None
    
    def test_config_with_file(self, sample_config_file):
        """Test loading configuration from file."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        config = Config(config_file=str(sample_config_file))
        
        # Check that values from file are loaded
        assert config.get('api.timeout') == 30
        assert config.get('api.max_retries') == 3
        assert config.get('api.base_url') == "https://api.example.com"
    
    def test_config_with_env_vars(self):
        """Test that environment variables override configuration."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        with patch.dict('os.environ', {'API_TIMEOUT': '60'}):
            config = Config()
            # Environment variable should override default (converted to int)
            assert config.get('api.timeout') == 60
    
    def test_config_hierarchy(self, sample_config_file):
        """Test configuration hierarchy: env vars > config file > defaults."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        with patch.dict('os.environ', {'API_TIMEOUT': '90'}):
            config = Config(config_file=str(sample_config_file))
            
            # Environment variable should win
            assert config.get('api.timeout') == '90'
            
            # File value should be used when no env var
            assert config.get('api.max_retries') == 3
            
            # Default should be used when neither file nor env var
            assert config.get('logging.level') is not None
    
    def test_get_config_singleton(self):
        """Test that get_config returns a singleton."""
        from src.{{cookiecutter.package_name}}.config import get_config
        
        config1 = get_config()
        config2 = get_config()
        
        assert config1 is config2
    
    def test_config_get_with_default(self):
        """Test getting configuration values with defaults."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        config = Config()
        
        # Non-existent key should return default
        assert config.get('non.existent.key', 'default_value') == 'default_value'
        
        # Non-existent key without default should return None
        assert config.get('another.non.existent.key') is None
    
    def test_config_invalid_file(self, temp_dir):
        """Test handling of invalid configuration file."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        # Create an invalid JSON file
        invalid_config = temp_dir / "invalid_config.json"
        invalid_config.write_text("{ invalid json content")
        
        # Should not raise exception, but log error and use defaults
        config = Config(config_file=str(invalid_config))
        assert config is not None
        # Should still have default values
        assert config.get('logging.level') is not None
    
    def test_config_missing_file(self):
        """Test handling when configuration file doesn't exist."""
        from src.{{cookiecutter.package_name}}.config import Config
        
        # Should not raise exception
        config = Config(config_file="non_existent_file.json")
        assert config is not None
        # Should still have default values
        assert config.get('logging.level') is not None
