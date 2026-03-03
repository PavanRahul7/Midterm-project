"""Tests for REPL and Config."""
import pytest
import tempfile
import os
from app.calculator_repl import CalculatorREPL
from app.calculator_config import CalculatorConfig

class TestCalculatorREPL:
    """Test REPL interface."""
    
    def test_repl_initialization(self):
        repl = CalculatorREPL()
        assert repl.calculator is not None

class TestCalculatorConfig:
    """Test configuration management."""
    
    def test_config_initialization(self):
        config = CalculatorConfig()
        assert config.log_dir is not None
        assert config.history_dir is not None
        assert config.log_file is not None
        assert config.history_file is not None
    
    def test_config_max_history_size(self):
        config = CalculatorConfig()
        assert config.max_history_size > 0
    
    def test_config_auto_save(self):
        config = CalculatorConfig()
        assert isinstance(config.auto_save, bool)
    
    def test_config_precision(self):
        config = CalculatorConfig()
        assert config.precision > 0
    
    def test_config_max_input_value(self):
        config = CalculatorConfig()
        assert config.max_input_value > 0
    
    def test_config_encoding(self):
        config = CalculatorConfig()
        assert config.encoding == 'utf-8'
