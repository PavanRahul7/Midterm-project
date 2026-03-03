# Midterm Project: Enhanced Calculator Command-Line Application 

A comprehensive Python calculator application demonstrating professional software engineering practices, including multiple design patterns, comprehensive testing, and production-ready code.

## 🎯 Features

### ✅ Core Functionality
- **6 Advanced Operations**: Power, Root, Modulus, Integer Division, Percentage, Absolute Difference
- **REPL Interface**: Interactive command-line calculator
- **History Management**: View, clear, and manage calculation history
- **Undo/Redo**: Revert and re-apply operations using Memento pattern
- **Auto-Save**: Automatic history persistence to CSV

### ✅ Design Patterns
- **Factory Pattern**: Dynamic operation creation
- **Observer Pattern**: LoggingObserver and AutoSaveObserver
- **Memento Pattern**: Undo/redo functionality
- **Singleton Pattern**: Configuration and Logger
- **Strategy Pattern**: Interchangeable operation strategies
- **Facade Pattern**: Unified calculator interface

### ✅ Professional Features
- **Comprehensive Logging**: File and console logging with rotating file handler
- **Configuration Management**: Environment variables with .env support
- **Input Validation**: Robust error handling with custom exceptions
- **Data Persistence**: CSV storage using pandas
- **Unit Testing**: 90%+ code coverage with pytest
- **CI/CD**: GitHub Actions workflow for automated testing
- **Documentation**: Complete README, docstrings, and type hints

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Setup

```bash
# Clone the repository (or extract if provided as ZIP)
git clone <repository-url>
cd module5_solution

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables (.env)

The application uses a `.env` file for configuration. Key variables:

```env
# Directories
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history

# Files
CALCULATOR_LOG_FILE=logs/calculator.log
CALCULATOR_HISTORY_FILE=history/calculations.csv

# History Settings
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true

# Calculation Settings
CALCULATOR_PRECISION=28
CALCULATOR_MAX_INPUT_VALUE=999999999
CALCULATOR_DEFAULT_ENCODING=utf-8
```

Modify `.env` to customize application behavior.

## 🚀 Usage

### Running the Calculator

```bash
python main.py
```

### REPL Commands

Once running, use these commands:

**Arithmetic Operations**:
```
add <a> <b>          - Addition
subtract <a> <b>     - Subtraction
multiply <a> <b>     - Multiplication
divide <a> <b>       - Division
power <a> <b>        - Exponentiation (a^b)
root <a> <b>         - Root (a^(1/b))
modulus <a> <b>      - Remainder (a % b)
int_divide <a> <b>   - Integer division (a // b)
percent <a> <b>      - Percentage ((a/b)*100)
abs_diff <a> <b>     - Absolute difference |a-b|
```

**History Management**:
```
history              - Show calculation history
clear                - Clear all history
undo                 - Undo last operation
redo                 - Redo last undone operation
save                 - Save history to file
load                 - Load history from file
```

**Utility**:
```
help                 - Show available commands
exit                 - Exit the application
```

### Example Session

```
> 10 add 5
Result: 15
> 20 multiply 3
Result: 60
> power 2 3
Result: 8
> history
1. 10 add 5 = 15
2. 20 multiply 3 = 60
3. 2 power 3 = 8
> undo
Undone: 2 power 3 = 8
> redo
Redone: 2 power 3 = 8
> exit
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_calculator.py
```

### Test Coverage

The project aims for **90%+ code coverage**. View the HTML coverage report:

```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html  # Open in browser
```

### Test Structure

- `test_calculator.py` - Main calculator class tests
- `test_calculation.py` - Calculation model tests
- `test_operations.py` - Operation and Factory pattern tests
- `test_history.py` - History and Observer pattern tests
- `test_validators.py` - Input validation tests

## 📊 Project Structure

```
module5_solution/
├── app/
│   ├── __init__.py
│   ├── calculator.py              # Main calculator (Facade pattern)
│   ├── calculation.py             # Calculation data model
│   ├── calculator_config.py       # Configuration (Singleton)
│   ├── calculator_memento.py      # State management (Memento)
│   ├── exceptions.py              # Custom exceptions
│   ├── history.py                 # History management (Observer)
│   ├── input_validators.py        # Input validation
│   ├── logger.py                  # Logging system
│   ├── operations.py              # Operations (Factory)
│   └── calculator_repl.py         # REPL interface
│
├── tests/
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_history.py
│   └── test_validators.py
│
├── .github/workflows/
│   └── python-app.yml             # GitHub Actions CI/CD
│
├── main.py                        # Entry point
├── requirements.txt               # Python dependencies
├── .env                          # Configuration file
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
└── STRUCTURE_AND_IMPLEMENTATION.md
```

## 🔧 Development

### Creating Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "Descriptive commit message"

# Push and create pull request
git push origin feature/your-feature
```

### Code Quality

- **Type Hints**: Full type annotations throughout
- **Docstrings**: Comprehensive module, class, and method documentation
- **DRY Principle**: Code reuse and modular design
- **Error Handling**: Custom exceptions with meaningful messages

## 📈 GitHub Actions CI/CD

The project includes a GitHub Actions workflow that:

1. Runs on every push to main branch
2. Executes all pytest tests
3. Measures code coverage
4. Enforces 90% coverage threshold
5. Fails if coverage is below threshold

View workflow status in the `Actions` tab of your GitHub repository.

## 📝 Logging

The application logs all events to a file and console:

- **Log File**: `logs/calculator.log`
- **Log Levels**: DEBUG, INFO, WARNING, ERROR
- **Rotating Handler**: Automatically manages log file size
- **Console Output**: Warnings and errors to console

Logs include:
- All calculations (operands, operation, result)
- Undo/redo operations
- History file operations
- Configuration loading
- Errors and exceptions

## 🔐 Error Handling

Custom exception hierarchy:
- `CalculatorError` - Base exception
- `ValidationError` - Input validation failures
- `OperationError` - Operation execution failures
- `ConfigurationError` - Configuration errors

All exceptions include meaningful error messages to guide users.

## 📚 Documentation

### Files
- **README.md** - Project overview and usage (this file)
- **STRUCTURE_AND_IMPLEMENTATION.md** - Technical implementation details
- **Code Docstrings** - Comprehensive documentation in source files
- **Type Hints** - Static type checking support

### Learning Resources
- Refactoring.Guru: [Design Patterns](https://refactoring.guru/design-patterns)
- Python Logging: [Official Documentation](https://docs.python.org/3/library/logging.html)
- Pandas CSV: [Official Documentation](https://pandas.pydata.org/docs/reference/frame.html#io)

## ✨ Optional Features (Grade A)

The project can be enhanced with:
- **Dynamic Help Menu** - Decorator pattern for automatic help generation
- **Color-Coded Outputs** - Using colorama for better UX
- **Command Pattern** - Encapsulating requests as objects

## 🐛 Troubleshooting

### Python Not Found
```bash
# Ensure Python 3.10+ is installed
python --version
# Download from python.org if needed
```

### Module Import Errors
```bash
# Ensure you're in the project root directory
cd module5_solution
# Reinstall dependencies
pip install -r requirements.txt
```

### Tests Failing
```bash
# Clear pytest cache
pytest --cache-clear
# Reinstall dependencies
pip install --upgrade -r requirements.txt
# Run with verbose output
pytest -v
```

### Permission Issues (Mac/Linux)
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

## 📞 Support

For questions or issues:
1. Check this README
2. Review the STRUCTURE_AND_IMPLEMENTATION.md
3. Check code docstrings and comments
4. Review test files for usage examples
5. Consult the Python and pandas documentation

## 📜 License

This project is provided as-is for educational purposes.

## 🎓 Learning Outcomes

By completing this project, you'll understand:
- Professional software architecture
- Design patterns in practice
- Comprehensive testing strategies
- Configuration management
- Logging and monitoring
- Error handling best practices
- Continuous integration/deployment
- Professional documentation

---

**Happy calculating!** 🎉

For any questions, refer to the code documentation and test files for examples of how to use the calculator.
