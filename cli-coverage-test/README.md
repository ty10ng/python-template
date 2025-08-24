# CLI Coverage Test

[![CI](https://github.com/your-username/cli-coverage-test/workflows/CI/badge.svg)](https://github.com/your-username/cli-coverage-test/actions/workflows/ci.yml)
[![Documentation](https://github.com/your-username/cli-coverage-test/workflows/Documentation/badge.svg)](https://your-username.github.io/cli-coverage-test)
[![CodeQL](https://github.com/your-username/cli-coverage-test/workflows/CodeQL%20Analysis/badge.svg)](https://github.com/your-username/cli-coverage-test/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/your-username/cli-coverage-test/badge)](https://securityscorecards.dev/viewer/?uri=github.com/your-username/cli-coverage-test)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A brief description of your project

## Features

- **🔍 Professional Logging**: Security-aware logging with sensitive data filtering
- **🔒 Audit Trail**: Security events and compliance logging
- **⚙️ Hierarchical Configuration**: YAML config files with environment variable overrides
- **🔍 Environment Validation**: Automatic checking of required vs optional environment variables
- **🧵 Thread Safety**: Safe concurrent operations throughout
- **🎨 Rich Output**: Colored console logs with emoji indicators
- **📝 JSON Formatting**: Structured JSON log output for production
- **📁 Best Practices**: Python packaging standards with src/ layout
- **🧪 Comprehensive Testing**: Full test suite with security and performance tests
- **⚡ Professional CLI**: Rich command-line interface with Click framework
- **🗂️ Shell Completion**: Auto-completion for bash, zsh, fish, and PowerShell
- **📖 Man Page Generation**: Automatic documentation for system integration
- **🎯 Smart Commands**: Context-aware commands with helpful error messages

## Quick Start

### Installation

```bash
# Clone your new project
git clone <your-repo-url>
cd cli-coverage-test

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Configuration

1. **Environment Setup**:

```bash
cp .env.example .env
# Edit .env with your configuration
```

2. **Configuration File** (optional):

```bash
# Copy example configuration
cp config.json config.local.json
# Edit config.local.json with your settings
```

### Usage

#### Command Line Interface

After installation, the CLI is available as `cli_coverage_test`:

```bash
# Get help
cli_coverage_test --help

# Check application status
cli_coverage_test status

# Say hello with options
cli_coverage_test hello "World" --count 3

# Show detailed application info
cli_coverage_test info

# Install shell completion (bash, zsh, fish, powershell)
cli_coverage_test --install-completion bash

# Show completion help
cli_coverage_test completion
```

#### Installation

```bash
# Install from PyPI (when published)
pip install cli-coverage-test

# Install from source
git clone https://github.com/your-username/cli-coverage-test
cd cli-coverage-test
pip install .

# Development installation
pip install -e ".[dev]"
```

#### Shell Completion

The CLI supports auto-completion for major shells:

```bash
# Bash
cli_coverage_test --install-completion bash
source ~/.bashrc

# Zsh  
cli_coverage_test --install-completion zsh
source ~/.zshrc

# Fish
cli_coverage_test --install-completion fish

# PowerShell
cli_coverage_test --install-completion powershell
```

#### Man Page

Generate and install a man page:

```bash
# Generate man page
cli_coverage_test-man

# Install system-wide (requires sudo)
sudo cp cli_coverage_test.1 /usr/local/man/man1/

# View man page
man cli_coverage_test
```

#### Programmatic Usage

```python
from cli_coverage_test import get_logger, get_config

# Professional logging
logger = get_logger(__name__)
logger.info("Application started")
logger.warning("This is a warning")
logger.error("Something went wrong")

# Hierarchical configuration
config = get_config()
api_timeout = config.get('api.timeout', 30)
debug_mode = config.get('app.debug', False)
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks (if included)
pre-commit install

```

### Alternative Dependency Management

While this project uses standard `pyproject.toml` + `pip` (recommended for maximum compatibility), you can adapt it to other tools:

#### **Poetry** (Popular Alternative)
```bash
# Convert to Poetry
poetry init --no-interaction
poetry add $(grep -E "^\s*\"" pyproject.toml | cut -d'"' -f2)
poetry install
```

#### **Pipenv** (If You Prefer It)
```bash
# Create Pipfile from pyproject.toml dependencies
pipenv install -e .
pipenv install --dev pytest pytest-cov black flake8 mypy
```

#### **pip-tools** (For Lock Files)
```bash
# Generate lock file from pyproject.toml
pip install pip-tools
pip-compile pyproject.toml
pip-sync requirements.txt
```

> **💡 Recommendation**: Stick with the default `pyproject.toml` + `pip` approach unless you have specific requirements. It's the modern Python standard and works everywhere.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=cli_coverage_test

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

## Configuration Management

### Environment Variables

The application uses a hierarchical configuration system:

**DEFAULTS < CONFIG_FILE < Environment Variables**

| Variable | Description | Required |
| -------- | ----------- | -------- |
| `CLI_COVERAGE_TEST_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | No |
| `CLI_COVERAGE_TEST_CONFIG_FILE` | Path to YAML configuration file | No |

### Configuration File

Create a `config.local.json` file:

```json
{
  "logging": {
    "level": "INFO",
    "console_level": "INFO",
    "file_level": "DEBUG"
  },
  "app": {
    "debug": false,
    "name": "CLI Coverage Test"
  }
}
```

## Project Structure

```
cli-coverage-test/
├── src/cli_coverage_test/     # Main package
│   ├── __init__.py           # Package exports
│   ├── config.py             # Configuration management
│   ├── core.py               # Application core logic
│   └── logger.py             # Professional logging system
├── tests/                    # Comprehensive test suite
│   ├── __init__.py           # Test package init
│   ├── test_config.py        # Configuration tests
│   └── test_core.py          # Core functionality tests
├── .env.example              # Environment template
├── config.json               # Configuration template
├── pyproject.toml            # Project configuration
└── README.md                 # Project documentation
```

## Security Features

### Sensitive Data Protection

The logging system automatically filters sensitive information:

- **Passwords**: `password=secret123` → `password=[REDACTED]`
- **API Keys**: `api_key=sk_test_123` → `api_key=[REDACTED]`
- **Tokens**: `token=abc123def456` → `token=[REDACTED]`
- **Credit Cards**: `4532-1234-5678-9012` → `[REDACTED]`
- **SSNs**: `123-45-6789` → `[REDACTED]`

### Audit Logging

Security events are automatically logged to `logs/audit.log`:

```python
from cli_coverage_test import get_logger

logger = get_logger(__name__)
logger.log_security_event('user_login', {
    'user_id': 'user123',
    'ip_address': '192.168.1.1',
    'success': True
})
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

**Your Name** - your.email@example.com

---

_Generated from the [Python Professional Template](https://github.com/your-username/python-template)_
