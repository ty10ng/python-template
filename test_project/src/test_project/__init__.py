"""
test_project package - A modular Python application framework.

This package provides centralized logging, hierarchical configuration management,
and environment variable validation for Python applications.
"""

from .logger import (
    get_logger,
    debug, info, warning, error, critical
)
from .config import get_config, reload_config
from .core import App, main

__version__ = "0.1.0"
__author__ = "Test Author"

__all__ = [
    "get_logger", "debug", "info", "warning", "error", "critical",
    "get_config", "reload_config",
    "App", "main"
]
