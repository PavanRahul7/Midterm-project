"""Configuration management for the calculator."""

import os
from dotenv import load_dotenv

class CalculatorConfig:
    """Manages configuration settings using environment variables."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        load_dotenv()
        
        # Base directories
        self.log_dir = os.getenv('CALCULATOR_LOG_DIR', 'logs')
        self.history_dir = os.getenv('CALCULATOR_HISTORY_DIR', 'history')
        
        # Files
        self.log_file = os.getenv('CALCULATOR_LOG_FILE', f'{self.log_dir}/calculator.log')
        self.history_file = os.getenv('CALCULATOR_HISTORY_FILE', f'{self.history_dir}/calculations.csv')
        
        # History settings
        try:
            self.max_history_size = int(os.getenv('CALCULATOR_MAX_HISTORY_SIZE', '100'))
        except ValueError:
            self.max_history_size = 100
        
        self.auto_save = os.getenv('CALCULATOR_AUTO_SAVE', 'true').lower() in ('true', '1', 'yes')
        
        # Calculation settings
        try:
            self.precision = int(os.getenv('CALCULATOR_PRECISION', '28'))
        except ValueError:
            self.precision = 28
        
        try:
            self.max_input_value = float(os.getenv('CALCULATOR_MAX_INPUT_VALUE', '999999999'))
        except ValueError:
            self.max_input_value = 999999999
        
        self.encoding = os.getenv('CALCULATOR_DEFAULT_ENCODING', 'utf-8')
        
        # Create directories
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)
