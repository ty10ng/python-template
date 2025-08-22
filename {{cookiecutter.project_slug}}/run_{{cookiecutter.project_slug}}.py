#!/usr/bin/env python3
"""
{{cookiecutter.project_name}} - {{cookiecutter.project_description}}

{% if cookiecutter.project_type == "cli" -%}
Command-line interface for {{cookiecutter.project_name}}.
{% elif cookiecutter.project_type == "api_server" -%}
API server application for {{cookiecutter.project_name}}.
{% elif cookiecutter.project_type == "microservice" -%}
Microservice application for {{cookiecutter.project_name}}.
{% else -%}
Main application entry point for {{cookiecutter.project_name}}.
{% endif -%}
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from {{cookiecutter.package_name}}.core import main


if __name__ == "__main__":
    main()
