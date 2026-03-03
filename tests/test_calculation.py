"""Tests for Calculation model."""
import pytest
from decimal import Decimal
from app.calculation import Calculation

class TestCalculation:
    """Test Calculation dataclass."""
    
    def test_calculation_creation(self):
        """Test creating a calculation."""
        calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        assert calc.a == Decimal('10')
        assert calc.b == Decimal('5')
        assert calc.operation == 'add'
        assert calc.result == Decimal('15')
    
    def test_calculation_with_int_conversion(self):
        """Test creation with int conversion."""
        calc = Calculation(10, 5, 'add', 15)
        assert isinstance(calc.a, Decimal)
        assert isinstance(calc.b, Decimal)
        assert isinstance(calc.result, Decimal)
    
    def test_calculation_to_dict(self):
        """Test converting to dictionary."""
        calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        data = calc.to_dict()
        assert data['a'] == '10'
        assert data['b'] == '5'
        assert data['operation'] == 'add'
        assert data['result'] == '15'
    
    def test_calculation_from_dict(self):
        """Test creating from dictionary."""
        data = {'a': '10', 'b': '5', 'operation': 'add', 'result': '15'}
        calc = Calculation.from_dict(data)
        assert calc.a == Decimal('10')
        assert calc.b == Decimal('5')
        assert calc.operation == 'add'
        assert calc.result == Decimal('15')
    
    def test_calculation_str_representation(self):
        """Test string representation."""
        calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        assert str(calc) == '10 add 5 = 15'
    
    def test_calculation_with_negative_numbers(self):
        """Test with negative numbers."""
        calc = Calculation(Decimal('-10'), Decimal('-5'), 'add', Decimal('-15'))
        assert calc.a == Decimal('-10')
        assert str(calc) == '-10 add -5 = -15'
    
    def test_calculation_with_decimals(self):
        """Test with decimal values."""
        calc = Calculation(Decimal('10.5'), Decimal('5.2'), 'add', Decimal('15.7'))
        assert calc.a == Decimal('10.5')
        assert calc.b == Decimal('5.2')
        assert calc.result == Decimal('15.7')
    
    def test_calculation_round_trip(self):
        """Test round-trip conversion."""
        original = Calculation(Decimal('3.14'), Decimal('2.71'), 'multiply', Decimal('8.51'))
        data = original.to_dict()
        restored = Calculation.from_dict(data)
        assert original.a == restored.a
        assert original.b == restored.b
        assert original.operation == restored.operation
        assert original.result == restored.result
