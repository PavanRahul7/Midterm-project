"""Additional tests for operations edge and error cases."""
import pytest
from decimal import Decimal
from app.operations import Divide, Root, Modulus, IntDivide, Percentage, OperationFactory
from app.exceptions import OperationError


def test_divide_by_zero():
    with pytest.raises(OperationError):
        Divide().execute(Decimal('1'), Decimal('0'))


def test_modulus_by_zero():
    with pytest.raises(OperationError):
        Modulus().execute(Decimal('1'), Decimal('0'))


def test_int_divide_by_zero():
    with pytest.raises(OperationError):
        IntDivide().execute(Decimal('1'), Decimal('0'))


def test_percentage_by_zero():
    with pytest.raises(OperationError):
        Percentage().execute(Decimal('1'), Decimal('0'))


def test_root_index_zero():
    with pytest.raises(OperationError):
        Root().execute(Decimal('4'), Decimal('0'))


def test_root_even_negative():
    with pytest.raises(OperationError):
        Root().execute(Decimal('-4'), Decimal('2'))


def test_root_non_integer_negative():
    with pytest.raises(OperationError):
        Root().execute(Decimal('-8'), Decimal('2.5'))


def test_operation_factory_unknown():
    with pytest.raises(OperationError):
        OperationFactory.get_operation('unknown')


def test_get_available_operations_sorted():
    ops = OperationFactory.get_available_operations()
    assert ops == sorted(ops)
