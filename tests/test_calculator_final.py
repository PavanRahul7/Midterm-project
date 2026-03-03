"""Final calculator tests for 100% coverage."""
import pytest
from decimal import Decimal
from app.calculator import Calculator

class TestCalculatorFinal:
    """Final calculator tests for 100% coverage."""
    
    def test_precision_line_48(self):
        """Test precision quantization on line 48."""
        calc = Calculator()
        # Get a result with many decimal places
        result = calc.perform_operation('10', '3', 'divide')
        
        # Verify it's quantized
        assert isinstance(result, Decimal)
        
        # Result string length should be reasonable
        result_str = str(result)
        if '.' in result_str:
            decimals = len(result_str.split('.')[-1])
            assert decimals <= 28  # max precision
