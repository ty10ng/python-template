"""
Core application module for test_project.

This module contains the main application logic and entry points.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from .logger import get_logger
from .config import get_config

# Initialize logger for this module
logger = get_logger(__name__)


class App:
    """Main application class for test_project."""

    def __init__(self):
        """Initialize the test_project application."""
        self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")
        self.logger.info("Initializing App")

        # Load environment variables
        load_dotenv()

        # Initialize configuration system (loads defaults, config file, env vars)
        self.config = get_config()

        # Check environment variables
        self._check_environment()

    def _check_environment(self):
        """Check and log environment variable status based on .env.example."""
        # Get the project root directory (where .env.example is located)
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent  # Go up from src/test_project/core.py to project root
        env_example_path = project_root / ".env.example"

        if not env_example_path.exists():
            self.logger.warning(f".env.example file not found at {env_example_path}")
            return

        # Parse .env.example file to extract variable names
        all_vars = self._parse_env_example(env_example_path)

        if not all_vars:
            self.logger.info("No environment variables defined in .env.example")
            return

        # Separate required and optional variables
        required_vars = {name: info for name, info in all_vars.items() if not info.get('optional', False)}
        optional_vars = {name: info for name, info in all_vars.items() if info.get('optional', False)}

        # Check each variable
        missing_required = []
        missing_optional = []
        present_vars = []

        for var_name, var_info in all_vars.items():
            value = os.getenv(var_name)
            if value:
                present_vars.append(var_name)
                status = "✅"
                if var_info.get('optional', False):
                    status += " (optional)"
                self.logger.info(f"{status} {var_name} found in environment")
            else:
                if var_info.get('optional', False):
                    missing_optional.append((var_name, var_info))
                    self.logger.debug(f"ℹ️  {var_name} (optional) not set in environment")
                else:
                    missing_required.append((var_name, var_info))
                    self.logger.warning(f"⚠️  {var_name} not found in environment variables")

        # Summary logging for required variables only
        if missing_required:
            self.logger.warning(f"Missing {len(missing_required)} required environment variable(s). "
                              f"Please check your .env file and ensure these are set:")
            for var_name, var_info in missing_required:
                desc_text = f" - {var_info.get('description', '')}" if var_info.get('description') else ""
                self.logger.warning(f"  • {var_name}{desc_text}")

        # Info logging for optional variables
        if missing_optional:
            self.logger.info(f"Optional environment variables not set: {', '.join([name for name, _ in missing_optional])}")

        if present_vars:
            self.logger.info(f"Found {len(present_vars)} environment variable(s): {', '.join(present_vars)}")

    def _parse_env_example(self, env_example_path: Path) -> dict:
        """
        Parse .env.example file to extract environment variable names and metadata.

        Returns:
            dict: Mapping of variable names to their metadata dict containing:
                  - description: Comment description (if any)
                  - optional: Boolean indicating if variable is optional
        """
        variables = {}

        try:
            with open(env_example_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            current_description = None
            is_optional = False

            for line in lines:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Handle comments
                if line.startswith('#'):
                    comment_text = line[1:].strip()

                    # Check for OPTIONAL marker
                    if comment_text.upper() == 'OPTIONAL':
                        is_optional = True
                        continue
                    # Only use non-empty comments as descriptions (but not OPTIONAL marker)
                    elif comment_text and not comment_text.startswith('=') and comment_text.upper() != 'OPTIONAL':
                        current_description = comment_text
                    continue

                # Handle variable definitions (VAR_NAME=value)
                if '=' in line and not line.startswith('#'):
                    var_name = line.split('=')[0].strip()
                    if var_name:
                        variables[var_name] = {
                            'description': current_description,
                            'optional': is_optional
                        }
                        # Reset state after using
                        current_description = None
                        is_optional = False

        except Exception as e:
            self.logger.error(f"Error parsing .env.example file: {e}")

        return variables

    def run(self):
        """Run the main application logic."""
        self.logger.info("Starting main application logic")

        try:
            # Your main application logic goes here
            self._process_data()

            self.logger.info("Application completed successfully")

        except Exception as e:
            self.logger.error(f"Application failed with error: {e}")
            raise

    def _process_data(self):
        """Example data processing method."""
        self.logger.debug("Processing application data")

        # Example: Use configuration values
        api_timeout = self.config.get('api.timeout', 30)
        max_retries = self.config.get('api.max_retries', 3)

        self.logger.info(f"Using API timeout: {api_timeout}s, max retries: {max_retries}")

        # Example processing logic
        data = {"example": "data", "config": {"timeout": api_timeout, "retries": max_retries}}
        self.logger.info(f"Processing data: {data}")

        # Simulate some work
        result = len(str(data))
        self.logger.debug(f"Processing result: {result}")

        return result


def main():
    """Main entry point for the application."""
    logger.info("Starting test_project application")

    try:
        app = App()
        app.run()

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.critical(f"Fatal error: {e}")


if __name__ == "__main__":
    main()
