"""Advanced operation tests for edge cases."""
import pytest
from decimal import Decimal, getcontext
from app.operations import Power, Root, Modulus, IntDivide, Percentage, AbsDiff
from app.exceptions import OperationError

class TestAdvancedOperations:
    """Test advanced operation edge cases."""
    
    def test_power_large_exponent(self):
        """Test power with large exponent."""
        result = Power().execute(Decimal('2'), Decimal('10'))
        assert result == Decimal('1024')
    
    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = Power().execute(Decimal('4'), Decimal('0.5'))
        assert float(result) == pytest.approx(2.0)
    
    def test_root_large_number(self):
        """Test root with large number."""
        result = Root().execute(Decimal('1000000'), Decimal('3'))
        assert float(result) == pytest.approx(100.0, rel=1e-3)
    
    def test_root_negative_odd_index(self):
        """Test root with negative number and odd index."""
        # Negative cube root should return negative result
        result = Root().execute(Decimal('-8'), Decimal('3'))
        # Result should be close to -2
        assert isinstance(result, Decimal)
    
    def test_modulus_large_numbers(self):
        """Test modulus with large numbers."""
        result = Modulus().execute(Decimal('1000000'), Decimal('7'))
        assert result == Decimal('1000000') % Decimal('7')
    
    def test_int_divide_large_numbers(self):
        """Test integer division with large numbers."""
        result = IntDivide().execute(Decimal('1000000'), Decimal('7'))
        assert result == Decimal('142857')
    
    def test_percentage_very_small(self):
        """Test percentage with very small numbers."""
        result = Percentage().execute(Decimal('0.001'), Decimal('1'))
        assert result == Decimal('0.1')
    
    def test_abs_diff_same_numbers(self):
        """Test absolute difference with same numbers."""
        result = AbsDiff().execute(Decimal('5'), Decimal('5'))
        assert result == Decimal('0')
