#!/usr/bin/env python3
"""
Test Project - A brief description of your project

Main application entry point for Test Project.
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from test_project.core import main


if __name__ == "__main__":
    main()
