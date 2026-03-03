"""Tests for operations and factory."""
import pytest
from decimal import Decimal
from app.operations import (
    Add, Subtract, Multiply, Divide, Power, Root,
    Modulus, IntDivide, Percentage, AbsDiff, OperationFactory
)
from app.exceptions import OperationError

class TestAdd:
    """Test Add operation."""
    def test_add_positive_numbers(self):
        assert Add().execute(Decimal('10'), Decimal('5')) == Decimal('15')
    def test_add_negative_numbers(self):
        assert Add().execute(Decimal('-10'), Decimal('-5')) == Decimal('-15')
    def test_add_mixed_signs(self):
        assert Add().execute(Decimal('10'), Decimal('-5')) == Decimal('5')

class TestSubtract:
    """Test Subtract operation."""
    def test_subtract_positive_numbers(self):
        assert Subtract().execute(Decimal('10'), Decimal('5')) == Decimal('5')
    def test_subtract_negative_result(self):
        assert Subtract().execute(Decimal('5'), Decimal('10')) == Decimal('-5')
    def test_subtract_negative_numbers(self):
        assert Subtract().execute(Decimal('-10'), Decimal('-5')) == Decimal('-5')

class TestMultiply:
    """Test Multiply operation."""
    def test_multiply_positive_numbers(self):
        assert Multiply().execute(Decimal('10'), Decimal('5')) == Decimal('50')
    def test_multiply_by_zero(self):
        assert Multiply().execute(Decimal('10'), Decimal('0')) == Decimal('0')
    def test_multiply_negative_numbers(self):
        assert Multiply().execute(Decimal('-10'), Decimal('-5')) == Decimal('50')

class TestDivide:
    """Test Divide operation."""
    def test_divide_positive_numbers(self):
        assert Divide().execute(Decimal('10'), Decimal('5')) == Decimal('2')
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(OperationError):
            Divide().execute(Decimal('10'), Decimal('0'))
    def test_divide_negative_numbers(self):
        assert Divide().execute(Decimal('-10'), Decimal('-5')) == Decimal('2')
    def test_divide_with_remainder(self):
        result = Divide().execute(Decimal('10'), Decimal('3'))
        assert float(result) == pytest.approx(3.333, rel=1e-3)

class TestPower:
    """Test Power operation."""
    def test_power_positive_exponent(self):
        assert Power().execute(Decimal('2'), Decimal('3')) == Decimal('8')
    def test_power_zero_exponent(self):
        assert Power().execute(Decimal('5'), Decimal('0')) == Decimal('1')
    def test_power_negative_exponent(self):
        result = Power().execute(Decimal('2'), Decimal('-2'))
        assert result == Decimal('0.25')

class TestRoot:
    """Test Root operation."""
    def test_square_root(self):
        assert Root().execute(Decimal('4'), Decimal('2')) == Decimal('2')
    def test_cube_root(self):
        result = Root().execute(Decimal('8'), Decimal('3'))
        assert float(result) == pytest.approx(2.0, rel=1e-5)
    def test_root_zero_index_raises_error(self):
        with pytest.raises(OperationError):
            Root().execute(Decimal('4'), Decimal('0'))
    def test_even_root_negative_raises_error(self):
        with pytest.raises(OperationError):
            Root().execute(Decimal('-4'), Decimal('2'))
    def test_root_of_one(self):
        assert Root().execute(Decimal('1'), Decimal('2')) == Decimal('1')

class TestModulus:
    """Test Modulus operation."""
    def test_modulus_positive_numbers(self):
        assert Modulus().execute(Decimal('10'), Decimal('3')) == Decimal('1')
    def test_modulus_by_zero_raises_error(self):
        with pytest.raises(OperationError):
            Modulus().execute(Decimal('10'), Decimal('0'))
    def test_modulus_negative_numbers(self):
        result = Modulus().execute(Decimal('-10'), Decimal('3'))
        assert result == Decimal('-1') or result == Decimal('2')  # Python behavior

class TestIntDivide:
    """Test Integer Division operation."""
    def test_int_divide_positive_numbers(self):
        assert IntDivide().execute(Decimal('10'), Decimal('3')) == Decimal('3')
    def test_int_divide_by_zero_raises_error(self):
        with pytest.raises(OperationError):
            IntDivide().execute(Decimal('10'), Decimal('0'))
    def test_int_divide_exact(self):
        assert IntDivide().execute(Decimal('10'), Decimal('5')) == Decimal('2')
    def test_int_divide_negative(self):
        # Python's // operator: -10 // 3 = -4 (floor division)
        result = IntDivide().execute(Decimal('-10'), Decimal('3'))
        assert result == Decimal('-4')

class TestPercentage:
    """Test Percentage operation."""
    def test_percentage_calculation(self):
        assert Percentage().execute(Decimal('50'), Decimal('100')) == Decimal('50')
    def test_percentage_by_zero_raises_error(self):
        with pytest.raises(OperationError):
            Percentage().execute(Decimal('50'), Decimal('0'))
    def test_percentage_decimal_result(self):
        result = Percentage().execute(Decimal('1'), Decimal('3'))
        assert float(result) == pytest.approx(33.33333, rel=1e-4)
    def test_percentage_above_100(self):
        result = Percentage().execute(Decimal('150'), Decimal('100'))
        assert result == Decimal('150')

class TestAbsDiff:
    """Test Absolute Difference operation."""
    def test_abs_diff_positive_numbers(self):
        assert AbsDiff().execute(Decimal('10'), Decimal('5')) == Decimal('5')
    def test_abs_diff_negative_result(self):
        assert AbsDiff().execute(Decimal('5'), Decimal('10')) == Decimal('5')
    def test_abs_diff_negative_numbers(self):
        assert AbsDiff().execute(Decimal('-10'), Decimal('-5')) == Decimal('5')
    def test_abs_diff_zero(self):
        assert AbsDiff().execute(Decimal('5'), Decimal('5')) == Decimal('0')

class TestOperationFactory:
    """Test OperationFactory."""
    
    def test_get_add_operation(self):
        op = OperationFactory.get_operation('add')
        assert isinstance(op, Add)
    
    def test_get_all_operations(self):
        ops = OperationFactory.get_available_operations()
        assert 'add' in ops
        assert 'subtract' in ops
        assert 'multiply' in ops
        assert 'divide' in ops
        assert 'power' in ops
        assert 'root' in ops
        assert 'modulus' in ops
        assert 'int_divide' in ops
        assert 'percent' in ops
        assert 'abs_diff' in ops
    
    def test_get_operation_case_insensitive(self):
        op1 = OperationFactory.get_operation('ADD')
        op2 = OperationFactory.get_operation('add')
        assert type(op1) == type(op2)
    
    def test_unknown_operation_raises_error(self):
        with pytest.raises(OperationError):
            OperationFactory.get_operation('unknown')
    
    def test_operations_are_sorted(self):
        ops = OperationFactory.get_available_operations()
        assert ops == sorted(ops)
    
    def test_get_each_operation(self):
        """Test getting each operation."""
        assert isinstance(OperationFactory.get_operation('add'), Add)
        assert isinstance(OperationFactory.get_operation('subtract'), Subtract)
        assert isinstance(OperationFactory.get_operation('multiply'), Multiply)
        assert isinstance(OperationFactory.get_operation('divide'), Divide)
        assert isinstance(OperationFactory.get_operation('power'), Power)
        assert isinstance(OperationFactory.get_operation('root'), Root)
        assert isinstance(OperationFactory.get_operation('modulus'), Modulus)
        assert isinstance(OperationFactory.get_operation('int_divide'), IntDivide)
        assert isinstance(OperationFactory.get_operation('percent'), Percentage)
        assert isinstance(OperationFactory.get_operation('abs_diff'), AbsDiff)
