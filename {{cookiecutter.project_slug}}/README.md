# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Features

- **🔍 Professional Logging**: Security-aware logging with sensitive data filtering
- **🔒 Audit Trail**: Security events and compliance logging
- **⚙️ Hierarchical Configuration**: YAML config files with environment variable overrides
- **🔍 Environment Validation**: Automatic checking of required vs optional environment variables
- **🧵 Thread Safety**: Safe concurrent operations throughout
- **🎨 Rich Output**: Colored console logs with emoji indicators
- **📝 JSON Formatting**: Structured JSON log output for production
- **📁 Best Practices**: Python packaging standards with src/ layout
- **🧪 Comprehensive Testing**: Full test suite with security and performance tests{% if cookiecutter.project_type == "cli-application" %}
- **⚡ Professional CLI**: Rich command-line interface with Click framework
- **🗂️ Shell Completion**: Auto-completion for bash, zsh, fish, and PowerShell
- **📖 Man Page Generation**: Automatic documentation for system integration
- **🎯 Smart Commands**: Context-aware commands with helpful error messages{% endif %}

## Quick Start

### Installation

```bash
# Clone your new project
git clone <your-repo-url>
cd {{cookiecutter.project_slug}}

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

{%- if cookiecutter.project_type == "cli-application" %}

#### Command Line Interface

After installation, the CLI is available as `{{ cookiecutter.package_name }}`:

```bash
# Get help
{{ cookiecutter.package_name }} --help

# Check application status
{{ cookiecutter.package_name }} status

# Say hello with options
{{ cookiecutter.package_name }} hello "World" --count 3

# Show detailed application info
{{ cookiecutter.package_name }} info

# Install shell completion (bash, zsh, fish, powershell)
{{ cookiecutter.package_name }} --install-completion bash

# Show completion help
{{ cookiecutter.package_name }} completion
```

#### Installation

```bash
# Install from PyPI (when published)
pip install {{ cookiecutter.project_slug }}

# Install from source
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
pip install .

# Development installation
pip install -e ".[dev]"
```

#### Shell Completion

The CLI supports auto-completion for major shells:

```bash
# Bash
{{ cookiecutter.package_name }} --install-completion bash
source ~/.bashrc

# Zsh  
{{ cookiecutter.package_name }} --install-completion zsh
source ~/.zshrc

# Fish
{{ cookiecutter.package_name }} --install-completion fish

# PowerShell
{{ cookiecutter.package_name }} --install-completion powershell
```

#### Man Page

Generate and install a man page:

```bash
# Generate man page
{{ cookiecutter.package_name }}-man

# Install system-wide (requires sudo)
sudo cp {{ cookiecutter.package_name }}.1 /usr/local/man/man1/

# View man page
man {{ cookiecutter.package_name }}
```

#### Programmatic Usage
{%- else %}

#### Library Usage
{%- endif %}

```python
from {{cookiecutter.package_name}} import get_logger, get_config

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
{% if cookiecutter.include_pre_commit == 'y' -%}
pre-commit install
{% endif %}
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov={{cookiecutter.package_name}}

# Run specific test categories
pytest tests/test_config.py
pytest tests/test_security.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

## Configuration Management

### Environment Variables

The application uses a hierarchical configuration system:

**DEFAULTS < CONFIG_FILE < Environment Variables**

| Variable | Description | Required |
| -------- | ----------- | -------- |
| `{{cookiecutter.package_name|upper}}_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | No |
| `{{cookiecutter.package_name|upper}}_CONFIG_FILE` | Path to YAML configuration file | No |

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
    "name": "{{cookiecutter.project_name}}"
  }
}
```

## Project Structure

```
{{cookiecutter.project_slug}}/
├── src/{{cookiecutter.package_name}}/     # Main package
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
from {{cookiecutter.package_name}} import get_logger

logger = get_logger(__name__)
logger.log_security_event('user_login', {
    'user_id': 'user123',
    'ip_address': '192.168.1.1',
    'success': True
})
```

## License

{% if cookiecutter.license != 'Private' -%}
This project is licensed under the {{cookiecutter.license}} License - see the LICENSE file for details.
{% else -%}
This project is private and proprietary.
{% endif %}

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

**{{cookiecutter.author_name}}** - {{cookiecutter.author_email}}

---

_Generated from the [Python Professional Template](https://github.com/{{cookiecutter.github_username}}/python-template)_
