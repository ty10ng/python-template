#!/usr/bin/env python3
"""
CLI Coverage Test - A brief description of your project
Command-line interface entry point for CLI Coverage Test.
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))
from cli_coverage_test.cli import main


if __name__ == "__main__":
    main()
