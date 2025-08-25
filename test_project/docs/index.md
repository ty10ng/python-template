# Test Project

A brief description of your project

## Features

- **🔍 Professional Logging**: Security-aware logging with sensitive data filtering
- **🔒 Audit Trail**: Security events and compliance logging
- **⚙️ Hierarchical Configuration**: YAML config files with environment variable overrides
- **🔍 Environment Validation**: Automatic checking of required vs optional environment variables
- **🧵 Thread Safety**: Safe concurrent operations throughout
- **🎨 Rich Output**: Colored console logs with structured JSON for production
- **📁 Best Practices**: Python packaging standards with src/ layout
- **🧪 Comprehensive Testing**: Full test suite with security and performance tests
- **⚡ Professional CLI**: Rich command-line interface with Click framework
- **🗂️ Shell Completion**: Auto-completion for bash, zsh, fish, and PowerShell
- **📖 Man Page Generation**: Automatic documentation for system integration

## Quick Start

### Installation

```bash
pip install test_project
```

### Command Line Usage

```bash
# Get help
test_project --help

# Basic usage examples
test_project status
test_project hello "World"
```

### Python Usage

```python
import test_project
from test_project import get_logger, get_config

# Get logger with automatic security filtering
logger = get_logger(__name__)
logger.info("Application started")

# Access configuration
config = get_config()
debug_mode = config.get('app.debug', False)
```

## Configuration

Test Project uses a hierarchical configuration system:

1. **Default values** (built into the application)
2. **Configuration file** (`config.yaml` in the project root)
3. **Environment variables** (highest priority)

### Configuration File

Create a `config.yaml` file in your project root:

```yaml
app:
  name: test_project
  debug: false

logging:
  level: INFO
  console_level: INFO
  file_level: DEBUG
  file_path: logs/test_project.log

# Add your custom configuration here
```

### Environment Variables

Override any configuration value with environment variables:

```bash
export TEST_PROJECT_APP_DEBUG=true
export TEST_PROJECT_LOGGING_LEVEL=DEBUG
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/ty10ng/test_project.git
cd test_project

# Install development dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=test_project

# Run specific test categories
pytest tests/test_config.py
pytest tests/test_security.py
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
mypy src/

# Run all pre-commit hooks
pre-commit run --all-files
```

## Project Structure

```
test_project/
├── src/test_project/     # Main package
│   ├── __init__.py           # Package exports
│   ├── config.py             # Configuration management
│   ├── core.py               # Application core logic
│   └── logger.py             # Professional logging system
├── tests/                    # Comprehensive test suite
│   ├── test_config.py        # Configuration tests
│   └── test_core.py          # Core functionality tests
├── docs/                     # Documentation source
├── config.yaml               # Configuration template
├── pyproject.toml            # Project configuration
└── README.md                 # Project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Contributing

See [Contributing Guide](contributing.md) for development guidelines.

## Author

**Test Author** - test@example.com

---

*Generated from the [Python Professional Template](https://github.com/ty10ng/python-template)*
