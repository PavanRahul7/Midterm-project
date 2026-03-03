"""Tests for Logger module."""
import pytest
import tempfile
import os
from app.logger import Logger

class TestLogger:
    """Test Logger singleton."""
    
    def test_logger_initialization(self):
        logger = Logger()
        assert logger.logger is not None
    
    def test_logger_singleton(self):
        logger1 = Logger()
        logger2 = Logger()
        assert logger1 is logger2
    
    def test_logger_info(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Reset logger for testing
            logger = Logger()
            logger.info("Test message")
    
    def test_logger_warning(self):
        logger = Logger()
        logger.warning("Test warning")
    
    def test_logger_error(self):
        logger = Logger()
        logger.error("Test error")
    
    def test_logger_debug(self):
        logger = Logger()
        logger.debug("Test debug")
