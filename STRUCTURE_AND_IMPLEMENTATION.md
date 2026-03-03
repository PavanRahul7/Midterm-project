# Module 5 Advanced Calculator - Complete Implementation Guide

## Project Requirements Implementation

This project implements ALL requirements from the Module 5 specifications:

### ✅ Core Requirements Implemented

#### 1. **Additional Arithmetic Operations** (6 Total)
- Power: a ** b
- Root: a ^ (1/b)  
- Modulus: a % b
- Integer Division: a // b
- Percentage: (a / b) * 100
- Absolute Difference: |a - b|

#### 2. **Design Patterns**
- **Factory Pattern**: OperationFactory creates operation instances
- **Observer Pattern**: LoggingObserver and AutoSaveObserver
- **Memento Pattern**: Undo/redo functionality
- **Singleton Pattern**: Configuration and Logger
- **Decorator Pattern**: (Optional) Dynamic help menu
- **Command Pattern**: (Optional) Encapsulated operations

#### 3. **History Management**
- Undo/Redo using Memento pattern
- CSV persistence using pandas
- Auto-save functionality
- History tracking with timestamps

#### 4. **Configuration Management**
- .env file support
- Environment variables for all settings
- Default value fallbacks
- Proper validation

#### 5. **Observer Pattern Implementation**
- LoggingObserver: Logs calculations to file
- AutoSaveObserver: Saves history to CSV
- Event notification system

#### 6. **Error Handling**
- Custom exception hierarchy
- Input validation
- Graceful error recovery
- Meaningful error messages

#### 7. **Logging System**
- Python logging module
- File and console handlers
- Appropriate logging levels
- Rotating file handler

#### 8. **REPL Command-Line Interface**
Supported commands:
- add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
- history, clear, undo, redo
- save, load
- help, exit

#### 9. **Testing**
- Pytest unit tests
- 90%+ code coverage
- Parameterized tests
- Edge case testing
- pytest-cov for coverage measurement

#### 10. **Data Persistence**
- Pandas DataFrame for history
- CSV serialization/deserialization
- Error handling for malformed files

#### 11. **GitHub Actions CI/CD**
- Automatic test execution on push
- Coverage enforcement (90% minimum)
- pytest-cov integration
- Workflow file included

#### 12. **Documentation**
- Comprehensive README.md
- Setup instructions
- Configuration guide
- Usage examples
- Testing instructions

### 📁 Project Structure

```
module5_solution/
├── app/
│   ├── __init__.py
│   ├── calculator.py              # Main calculator class
│   ├── calculation.py             # Calculation model
│   ├── calculator_config.py       # Configuration (Singleton)
│   ├── calculator_memento.py      # Memento pattern
│   ├── exceptions.py              # Exception hierarchy
│   ├── history.py                 # History management
│   ├── input_validators.py        # Input validation
│   ├── operations.py              # Operations (Factory, Strategy)
│   ├── logger.py                  # Logging system
│   └── calculator_repl.py         # REPL interface
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_history.py
│   └── test_validators.py
│
├── .github/
│   └── workflows/
│       └── python-app.yml         # CI/CD configuration
│
├── main.py                        # Entry point
├── requirements.txt               # Dependencies
├── .env                          # Configuration file
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
└── STRUCTURE_AND_IMPLEMENTATION.md  # This file
```

### 🎯 Key Implementation Details

#### Operations (6 Required + Base Framework)
Each operation:
- Takes exactly 2 numerical inputs
- Returns correct result
- Handles edge cases (division by zero, negative roots, etc.)
- Uses Factory pattern for instantiation

#### Observer Pattern
- **LoggingObserver**: Logs calculation details with timestamps
- **AutoSaveObserver**: Automatically saves to CSV
- Both registered with Calculator
- Respond to calculation events

#### Configuration (.env)
```
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_LOG_FILE=logs/calculator.log
CALCULATOR_HISTORY_FILE=history/calculations.csv
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=28
CALCULATOR_MAX_INPUT_VALUE=999999999
CALCULATOR_DEFAULT_ENCODING=utf-8
```

#### Undo/Redo (Memento Pattern)
- Maintains state history
- Allows reverting and re-applying operations
- Accurate stack management
- Handles edge cases

#### Testing Coverage
- 90%+ code coverage required
- Comprehensive test suite
- Parameterized tests for efficiency
- Edge case and error condition testing
- pragma: no cover for intentional exclusions

#### GitHub Actions
- Automated test execution
- Coverage enforcement (90%)
- Runs on every push to main
- Comprehensive CI/CD pipeline

### 🚀 Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python main.py

# Test
pytest
pytest --cov=app --cov-report=html
```

### 📝 Module Descriptions

**calculator.py**: Main facade class coordinating all subsystems
**operations.py**: Factory pattern for operation creation
**calculator_memento.py**: State snapshots for undo/redo
**history.py**: History management with observers
**calculator_config.py**: Configuration management (Singleton)
**logger.py**: Logging system
**input_validators.py**: Input validation and error handling
**calculation.py**: Calculation data model
**calculator_repl.py**: Command-line interface
**exceptions.py**: Custom exception hierarchy

### ✨ Optional Features (For Grade A)

At least ONE of the following:
- Dynamic Help Menu (Decorator Pattern)
- Color-Coded Outputs (Colorama)
- Additional Design Patterns (Command Pattern)

### 📊 Expected Test Results

```
Tests: 50+ comprehensive tests
Coverage: 90%+
Execution: Fast (<10 seconds)
All tests: PASSING ✅
```

### 🔧 Git History

Project includes proper git history with:
- Regular commits with clear messages
- Feature branch development
- Documented progress
- Academic integrity compliance

This implementation is complete and production-ready!
