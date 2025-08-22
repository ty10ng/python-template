# ty10ng's Python Project Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-blue.svg)](https://github.com/cookiecutter/cookiecutter)

My personal [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects. This is a living template that evolves as I learn and develop better patterns for Python development. It includes the foundations I've found useful in my own projects - feel free to use it if it helps your projects too!

> **🎯 Goal**: Provide a solid, opinionated foundation for Python projects with security, testing, and configuration best practices built-in.

> **📝 Note**: This template reflects my current understanding and preferred patterns. It will continue to evolve as I discover new tools, techniques, and best practices in Python development.

## What This Template Provides

### 🔒 Security-Conscious Logging

- **Sensitive data filtering**: Automatically masks passwords, tokens, and secrets in logs
- **Structured log formatting**: Consistent, readable log output
- **Multiple log handlers**: Console and file logging with rotation

### ⚙️ Flexible Configuration Management

- **Hierarchical configuration**: Environment variables → Config file → Defaults
- **Easy access patterns**: Dotted notation like `config.get('api.timeout')`
- **Environment validation**: Checks for required variables on startup

### 🧪 Testing Foundation

- **pytest setup**: Ready-to-use testing infrastructure
- **Helpful fixtures**: Common testing utilities for config and environment mocking
- **Example tests**: Patterns I've found useful for testing Python applications

### 🚀 Project Structure Options

- **Library**: Standard Python package for reusable code
- **CLI Application**: Command-line tools with proper argument handling
- **API Server**: Basic structure for REST APIs
- **Microservice**: Foundation for containerized services

> **Why these features?** These are patterns I've developed through building various Python projects. They solve common problems I encounter and provide a solid foundation for new projects.

## Quick Start

### Prerequisites

```bash
pip install cookiecutter
```

### Generate Your Project

```bash
cookiecutter https://github.com/ty10ng/python-template.git
```

You'll be prompted for project details like name, description, and which features to include.

### Example Usage

```bash
$ cookiecutter https://github.com/ty10ng/python-template.git

project_name [My Python Project]: Data Analysis Tool
project_slug [data-analysis-tool]: 
package_name [data_analysis_tool]: 
project_description [A brief description of your project]: Tool for analyzing research data
python_version [3.11]: 
project_type [library]: cli-application
author_name [Your Name]: Tyler Long
author_email [your.email@example.com]: ty@example.com
github_username [your-username]: ty10ng
include_docker [y]: n
include_github_actions [y]: y
include_pre_commit [y]: y
license [MIT]: 
```

## Generated Project Structure

```
data-analysis-tool/
├── src/
│   └── data_analysis_tool/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Main application logic
│       ├── config.py            # Configuration management
│       └── logger.py            # Security-aware logging
├── tests/
│   ├── __init__.py              # Test package initialization
│   ├── test_core.py             # Core functionality tests
│   └── test_config.py           # Configuration tests
├── .env.example                 # Environment variables template
├── config.json                  # Default configuration
├── pyproject.toml              # Project metadata and dependencies
├── README.md                   # Generated project documentation
└── run_data-analysis-tool.py   # CLI entry point
```

## Key Components

### Configuration System (`config.py`)

```python
from data_analysis_tool.config import get_config

config = get_config()
api_timeout = config.get('api.timeout', 30)  # Fallback to 30
database_url = config.get('database.url')    # From env or config file
```

**Configuration Hierarchy** (highest priority first):

1. Environment variables (e.g., `API_TIMEOUT`)
2. Configuration file (`config.json`)
3. Default values

### Security-Aware Logging (`logger.py`)

```python
from data_analysis_tool.logger import get_logger

logger = get_logger(__name__)
logger.info("Processing user request", extra={
    'user_id': 'user123',      # ✅ Safe to log
    'password': 'secret123'    # ❌ Automatically masked
})
```

**Security Features**:

- Automatic masking of sensitive fields (password, token, key, secret)
- Configurable allowed fields for logging
- Consistent formatting across all modules

### Environment Management

The template includes comprehensive environment variable management:

```bash
# .env.example shows required and optional variables
# Required variables
DATABASE_URL=postgresql://localhost/mydb

# OPTIONAL
# Optional feature flags
FEATURE_ENABLED=false
```

**Environment Checking**:

- Validates required variables on startup
- Logs missing required variables as warnings
- Logs optional variables as info
- Supports inline documentation

### Testing Infrastructure

```python
# tests/conftest.py provides useful fixtures
def test_my_feature(mock_env_vars, temp_dir, sample_config_file):
    # Test with isolated environment
    pass
```

**Test Features**:

- Environment variable mocking
- Temporary directory creation
- Sample configuration files
- Isolated test environments

## Project Types & Examples

The template supports different project types to match your specific needs:

### 📚 **Library** (Default)
Perfect for reusable packages and utilities.

**Example**: Data processing library, API client, utility functions
```bash
cookiecutter https://github.com/ty10ng/python-template.git
# Choose: project_type = library
```

**Generated structure**: Standard Python package with testing and configuration

### ⚡ **CLI Application**
Command-line tools with professional features.

**Example**: File processor, data converter, system utility
```bash
cookiecutter https://github.com/ty10ng/python-template.git
# Choose: project_type = cli-application
```

**Features included**:
- Click framework with Rich output
- Shell completion for bash/zsh/fish/PowerShell
- Man page generation
- Professional help system

**Usage example**:
```bash
your-tool --help
your-tool process-files *.csv --output results/
your-tool completion  # Setup shell completion
```

### 🚀 **Future Types**
Planning to add API server and microservice templates based on real project needs.

## Development Workflow

### 1. Initial Setup

```bash
cd your-new-project
pip install -e ".[dev]"              # Install in development mode
cp .env.example .env                 # Create environment file
# Edit .env with your values
```

### 2. Development

```bash
python your-project.py               # Run main application
python -m pytest                    # Run tests
python -m pytest --cov              # Run with coverage
```

### 3. Configuration

Edit `config.json` for default settings:

```json
{
  "api": {
    "timeout": 30,
    "base_url": "https://api.example.com"
  },
  "logging": {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  }
}
```

Override with environment variables:

```bash
export API_TIMEOUT=60
export LOG_LEVEL=DEBUG
```

## Project Types

This template supports multiple project types, each tailored for specific use cases:

### Library

- **Standard Python package structure** with modern packaging (pyproject.toml)
- **Importable modules and functions** with proper package initialization
- **Comprehensive configuration management** with environment variable support
- **Security-aware logging** with configurable levels and safe output
- **Testing framework** with pytest and coverage reporting
- **Code quality tools** (black, flake8, mypy) with sensible defaults
- **Development workflow** with optional GitHub Actions, Docker, and pre-commit hooks

### CLI Application

All library features plus:
- **Click-based command-line interface** with rich help formatting
- **Rich console output** with tables, colors, and progress indicators
- **Automatic entry point** installation via `pip install`
- **Professional CLI structure** with commands, options, and error handling
- **Built-in commands**: `status`, `hello`, `info` with extensible command structure

Example CLI usage:
```bash
# After installation
my-tool --help
my-tool status
my-tool hello "World" --count 3

# Or run directly
python run_my_project.py --help
```

### Future Expansions

Planned additions include:

- **API Server type**: FastAPI-based REST services with proper routing and documentation
- **Microservice type**: Containerized services with health checks and service discovery

Each type builds upon the core library foundation while adding specialized dependencies, entry points, and starter files.

## Best Practices

### Security

- ✅ Never log sensitive data directly
- ✅ Use environment variables for secrets
- ✅ Validate configuration on startup
- ✅ Use the provided logging utilities

### Configuration

- ✅ Use the hierarchical configuration system
- ✅ Document all variables in `.env.example`
- ✅ Provide sensible defaults in `config.json`
- ✅ Validate required configuration early

### Testing

- ✅ Use the provided test fixtures
- ✅ Test configuration scenarios
- ✅ Mock external dependencies
- ✅ Maintain high test coverage

## Template Evolution

This template is a living project that evolves with my Python development journey. As I discover new patterns, tools, or techniques that improve my development workflow, I'll incorporate them here.

### Current Focus Areas
- **Better testing patterns** - Exploring property-based testing and test automation
- **Development tooling** - Integrating more helpful pre-commit hooks and formatting tools  
- **Documentation** - Finding better ways to maintain project documentation
- **Performance** - Adding profiling and performance monitoring patterns

### Future Considerations
- Container deployment patterns (when I work more with Docker/Kubernetes)
- API design patterns (as I build more REST APIs)
- Database integration patterns (when projects need persistence)
- Monitoring and observability (for production deployments)

> **Note**: Features get added when I actually need them in my projects, not just because they're trendy. This keeps the template practical and focused.

## Development Approach

This template was developed collaboratively with AI as a coding partner, bringing together human experience and AI perspective to create something better than either could build alone. The patterns and decisions remain under continuous review to ensure they serve real project needs.

I believe in treating AI as a respectful collaborator - like working alongside a friend with a unique perspective. All design decisions ultimately reflect my development philosophy and real-world project experience.

## Contributing

I welcome contributions, feedback, and suggestions! This template improves through real-world usage and community input.

### 🐛 **Found a Bug?**
- Check [existing issues](https://github.com/ty10ng/python-template/issues) first
- Open a new issue with details about the problem
- Include steps to reproduce and your environment

### 💡 **Have an Idea?**
- Open an issue to discuss new features or improvements
- Explain the use case and how it would help your projects
- Consider if it fits the template's philosophy of practical, needed features

### 🔧 **Want to Contribute Code?**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Test your changes with both project types (library and CLI)
4. Commit with clear messages (`git commit -m 'Add amazing feature'`)
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### 📖 **Documentation Improvements**
Documentation improvements are always welcome! This includes:
- Better examples and use cases
- Clearer setup instructions
- More comprehensive troubleshooting

## License

This template is released under the [MIT License](LICENSE). Feel free to use it for any purpose, modify it to fit your needs, and share it with others.

## Acknowledgments

- Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Developed collaboratively with AI as a coding partner
- Inspired by real-world Python development challenges and solutions

---

**Happy coding!** 🐍✨

## License

This template is released under the MIT License. Projects generated from this template can use any license you prefer.

---

**A personal template by [@ty10ng](https://github.com/ty10ng) - evolving with each Python project**
