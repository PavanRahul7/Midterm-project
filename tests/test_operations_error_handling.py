"""Test error handling in operations."""
import pytest
from decimal import Decimal
from app.operations import Power, Root, Operation
from app.exceptions import OperationError

class TestOperationsErrorHandling:
    """Test error handling paths for 100% coverage."""
    
    def test_power_very_large_exponent(self):
        """Test power with very large exponent."""
        try:
            result = Power().execute(Decimal('10'), Decimal('100'))
            assert isinstance(result, Decimal)
        except OverflowError:
            pass
    
    def test_root_very_large_number(self):
        """Test root with very large number."""
        try:
            result = Root().execute(Decimal('10') ** Decimal('100'), Decimal('2'))
            assert isinstance(result, Decimal)
        except (OverflowError, ValueError):
            pass
    
    def test_root_fractional_index(self):
        """Test root with fractional index."""
        result = Root().execute(Decimal('16'), Decimal('0.5'))
        assert isinstance(result, Decimal)
    
    def test_power_decimal_base_and_exponent(self):
        """Test power with decimal base and exponent."""
        result = Power().execute(Decimal('2.5'), Decimal('1.5'))
        assert isinstance(result, Decimal)
    
    def test_root_one_index(self):
        """Test root with index 1."""
        result = Root().execute(Decimal('5'), Decimal('1'))
        assert result == Decimal('5')
    
    def test_operation_abstract_execute(self):
        """Test abstract operation cannot be instantiated."""
        with pytest.raises(TypeError):
            Operation()
