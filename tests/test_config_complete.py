"""Complete tests for configuration management."""
import pytest
import os
from unittest.mock import patch
from app.calculator_config import CalculatorConfig

class TestCalculatorConfigComplete:
    """Complete configuration tests for 100% coverage."""
    
    def test_config_default_log_dir(self):
        """Test default log directory."""
        config = CalculatorConfig()
        assert config.log_dir == 'logs'
    
    def test_config_default_history_dir(self):
        """Test default history directory."""
        config = CalculatorConfig()
        assert config.history_dir == 'history'
    
    def test_config_default_log_file(self):
        """Test default log file."""
        config = CalculatorConfig()
        assert 'calculator.log' in config.log_file
    
    def test_config_default_history_file(self):
        """Test default history file."""
        config = CalculatorConfig()
        assert 'calculations.csv' in config.history_file
    
    def test_config_auto_save_true_string(self):
        """Test auto save with 'true' string."""
        with patch.dict(os.environ, {'CALCULATOR_AUTO_SAVE': 'true'}):
            # Force reload
            config = CalculatorConfig()
            assert config.auto_save is True
    
    def test_config_auto_save_false_string(self):
        """Test auto save with 'false' string."""
        with patch.dict(os.environ, {'CALCULATOR_AUTO_SAVE': 'false'}):
            config = CalculatorConfig()
            assert config.auto_save is False
    
    def test_config_auto_save_one_string(self):
        """Test auto save with '1' string."""
        with patch.dict(os.environ, {'CALCULATOR_AUTO_SAVE': '1'}):
            config = CalculatorConfig()
            assert config.auto_save is True
    
    def test_config_auto_save_zero_string(self):
        """Test auto save with '0' string."""
        with patch.dict(os.environ, {'CALCULATOR_AUTO_SAVE': '0'}):
            config = CalculatorConfig()
            assert config.auto_save is False
    
    def test_config_invalid_max_history_size(self):
        """Test invalid max history size falls back to default."""
        with patch.dict(os.environ, {'CALCULATOR_MAX_HISTORY_SIZE': 'invalid'}):
            config = CalculatorConfig()
            assert config.max_history_size == 100  # Default
    
    def test_config_invalid_precision(self):
        """Test invalid precision falls back to default."""
        with patch.dict(os.environ, {'CALCULATOR_PRECISION': 'invalid'}):
            config = CalculatorConfig()
            assert config.precision == 28  # Default
    
    def test_config_invalid_max_input_value(self):
        """Test invalid max input value falls back to default."""
        with patch.dict(os.environ, {'CALCULATOR_MAX_INPUT_VALUE': 'invalid'}):
            config = CalculatorConfig()
            assert config.max_input_value == 999999999  # Default
    
    def test_config_creates_directories(self):
        """Test that config creates required directories."""
        config = CalculatorConfig()
        assert os.path.exists(config.log_dir)
        assert os.path.exists(config.history_dir)
    
    def test_config_custom_log_dir(self):
        """Test custom log directory from env."""
        with patch.dict(os.environ, {'CALCULATOR_LOG_DIR': 'custom_logs'}):
            config = CalculatorConfig()
            assert 'custom_logs' in config.log_dir
    
    def test_config_custom_history_dir(self):
        """Test custom history directory from env."""
        with patch.dict(os.environ, {'CALCULATOR_HISTORY_DIR': 'custom_history'}):
            config = CalculatorConfig()
            assert 'custom_history' in config.history_dir
    
    def test_config_custom_max_history_size(self):
        """Test custom max history size."""
        with patch.dict(os.environ, {'CALCULATOR_MAX_HISTORY_SIZE': '50'}):
            config = CalculatorConfig()
            assert config.max_history_size == 50
    
    def test_config_custom_precision(self):
        """Test custom precision."""
        with patch.dict(os.environ, {'CALCULATOR_PRECISION': '10'}):
            config = CalculatorConfig()
            assert config.precision == 10
    
    def test_config_custom_max_input_value(self):
        """Test custom max input value."""
        with patch.dict(os.environ, {'CALCULATOR_MAX_INPUT_VALUE': '1000'}):
            config = CalculatorConfig()
            assert config.max_input_value == 1000.0
