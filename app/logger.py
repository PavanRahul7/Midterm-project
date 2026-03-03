"""Logging configuration for the calculator."""

import logging
import os
from logging.handlers import RotatingFileHandler
from app.calculator_config import CalculatorConfig

class Logger:
    """Manages logging for the calculator application."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.config = CalculatorConfig()
        self.logger = logging.getLogger('calculator')
        self.logger.setLevel(logging.DEBUG)
        
        # Create logs directory if it doesn't exist
        os.makedirs(self.config.log_dir, exist_ok=True)
        
        # File handler
        handler = RotatingFileHandler(
            self.config.log_file,
            maxBytes=10485760,  # 10MB
            backupCount=5
        )
        handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
        self.logger.addHandler(console_handler)
        self._initialized = True
    
    def info(self, message):
        """Log info level message."""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning level message."""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error level message."""
        self.logger.error(message)
    
    def debug(self, message):
        """Log debug level message."""
        self.logger.debug(message)
