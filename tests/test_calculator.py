"""Tests for Calculator class."""
import pytest
import tempfile
import os
from decimal import Decimal
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError

class TestCalculator:
    """Test Calculator class."""
    
    def test_calculator_initialization(self):
        calc = Calculator()
        assert calc.factory is not None
        assert calc.history_manager is not None
        assert calc.memento_caretaker is not None
    
    def test_perform_addition(self):
        calc = Calculator()
        result = calc.perform_operation('10', '5', 'add')
        assert result == Decimal('15')
    
    def test_perform_subtraction(self):
        calc = Calculator()
        result = calc.perform_operation('10', '5', 'subtract')
        assert result == Decimal('5')
    
    def test_perform_multiplication(self):
        calc = Calculator()
        result = calc.perform_operation('10', '5', 'multiply')
        assert result == Decimal('50')
    
    def test_perform_division(self):
        calc = Calculator()
        result = calc.perform_operation('10', '5', 'divide')
        assert result == Decimal('2')
    
    def test_division_by_zero_raises_error(self):
        calc = Calculator()
        with pytest.raises(OperationError):
            calc.perform_operation('10', '0', 'divide')
    
    def test_perform_power(self):
        calc = Calculator()
        result = calc.perform_operation('2', '3', 'power')
        assert result == Decimal('8')
    
    def test_perform_root(self):
        calc = Calculator()
        result = calc.perform_operation('4', '2', 'root')
        assert result == Decimal('2')
    
    def test_perform_modulus(self):
        calc = Calculator()
        result = calc.perform_operation('10', '3', 'modulus')
        assert result == Decimal('1')
    
    def test_perform_int_divide(self):
        calc = Calculator()
        result = calc.perform_operation('10', '3', 'int_divide')
        assert result == Decimal('3')
    
    def test_perform_percent(self):
        calc = Calculator()
        result = calc.perform_operation('50', '100', 'percent')
        assert result == Decimal('50')
    
    def test_perform_abs_diff(self):
        calc = Calculator()
        result = calc.perform_operation('10', '15', 'abs_diff')
        assert result == Decimal('5')
    
    def test_invalid_operation_raises_error(self):
        calc = Calculator()
        with pytest.raises(ValidationError):
            calc.perform_operation('10', '5', 'invalid')
    
    def test_invalid_input_raises_error(self):
        calc = Calculator()
        with pytest.raises(ValidationError):
            calc.perform_operation('abc', '5', 'add')
    
    def test_undo_operation(self):
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        
        result = calc.undo()
        assert result is not None
        assert result.operation == 'add'
    
    def test_redo_operation(self):
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        
        calc.undo()
        result = calc.redo()
        assert result is not None
        assert result.operation == 'multiply'
    
    def test_can_undo(self):
        calc = Calculator()
        assert calc.can_undo() is False
        calc.perform_operation('10', '5', 'add')
        assert calc.can_undo() is False
        calc.perform_operation('15', '3', 'multiply')
        assert calc.can_undo() is True
    
    def test_can_redo(self):
        calc = Calculator()
        assert calc.can_redo() is False
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        calc.undo()
        assert calc.can_redo() is True
    
    def test_get_history(self):
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        
        history = calc.get_history()
        assert len(history) == 2
    
    def test_clear_history(self):
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.clear_history()
        assert len(calc.get_history()) == 0
    
    def test_save_history(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            calc = Calculator()
            calc.perform_operation('10', '5', 'add')
            
            filepath = os.path.join(tmpdir, 'history.csv')
            calc.save_history(filepath)
            assert os.path.exists(filepath)
    
    def test_load_history(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, 'history.csv')
            
            # Save history
            calc1 = Calculator()
            calc1.perform_operation('10', '5', 'add')
            calc1.save_history(filepath)
            
            # Load history
            calc2 = Calculator()
            calc2.load_history(filepath)
            history = calc2.get_history()
            assert len(history) == 1
    
    def test_get_available_operations(self):
        calc = Calculator()
        ops = calc.get_available_operations()
        assert 'add' in ops
        assert 'power' in ops
