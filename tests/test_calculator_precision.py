"""Test calculator precision handling."""
import pytest
from decimal import Decimal
from app.calculator import Calculator

class TestCalculatorPrecision:
    """Test precision quantization in calculator."""
    
    def test_calculator_precision_quantization(self):
        """Test that results are quantized to precision."""
        calc = Calculator()
        # Division often produces many decimal places
        result = calc.perform_operation('1', '3', 'divide')
        
        # Result should be quantized based on config precision
        result_str = str(result)
        if '.' in result_str:
            decimal_places = len(result_str.split('.')[-1])
            assert decimal_places <= calc.config.precision
    
    def test_calculator_handles_exact_decimal(self):
        """Test calculator with exact decimal result."""
        calc = Calculator()
        result = calc.perform_operation('10', '5', 'divide')
        assert result == Decimal('2')
    
    def test_calculator_multiple_precision_operations(self):
        """Test multiple operations with precision."""
        calc = Calculator()
        
        result1 = calc.perform_operation('1', '3', 'divide')  # High precision result
        result2 = calc.perform_operation('1', '3', 'percent')  # Percentage
        result3 = calc.perform_operation('1', '7', 'divide')  # Another repeating decimal
        
        # All should be valid Decimals
        assert isinstance(result1, Decimal)
        assert isinstance(result2, Decimal)
        assert isinstance(result3, Decimal)
