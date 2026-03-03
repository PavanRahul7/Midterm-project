"""Additional comprehensive calculator tests for 100% coverage."""
import pytest
import tempfile
import os
from decimal import Decimal
from app.calculator import Calculator
from app.calculation import Calculation
from app.exceptions import OperationError, ValidationError

class TestCalculatorEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_calculator_precision_handling(self):
        """Test precision quantization."""
        calc = Calculator()
        result = calc.perform_operation('1', '3', 'divide')
        assert isinstance(result, Decimal)
    
    def test_undo_with_no_operations(self):
        """Test undo when no operations performed."""
        calc = Calculator()
        result = calc.undo()
        assert result is None
    
    def test_redo_with_no_undone(self):
        """Test redo when nothing undone."""
        calc = Calculator()
        result = calc.redo()
        assert result is None
    
    def test_save_history_creates_file(self):
        """Test save history creates CSV file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, 'test.csv')
            calc = Calculator()
            calc.perform_operation('10', '5', 'add')
            calc.save_history(filepath)
            assert os.path.exists(filepath)
    
    def test_multiple_operations_sequence(self):
        """Test sequence of different operations."""
        calc = Calculator()
        results = []
        
        results.append(calc.perform_operation('10', '5', 'add'))
        results.append(calc.perform_operation('15', '3', 'subtract'))
        results.append(calc.perform_operation('12', '4', 'multiply'))
        results.append(calc.perform_operation('48', '6', 'divide'))
        
        assert len(calc.get_history()) == 4
        assert results[0] == Decimal('15')
        assert results[1] == Decimal('12')
        assert results[2] == Decimal('48')
        assert results[3] == Decimal('8')
    
    def test_calculator_with_large_numbers(self):
        """Test with large numbers."""
        calc = Calculator()
        result = calc.perform_operation('1000000000', '1000000000', 'add')
        assert result == Decimal('2000000000')
    
    def test_calculator_with_small_decimals(self):
        """Test with very small decimal numbers."""
        calc = Calculator()
        result = calc.perform_operation('0.0001', '0.0002', 'add')
        assert result == Decimal('0.0003')
    
    def test_invalid_input_caught(self):
        """Test invalid input error handling."""
        calc = Calculator()
        with pytest.raises(ValidationError):
            calc.perform_operation('invalid', '5', 'add')
    
    def test_calculation_str_with_decimal_operation(self):
        """Test string representation of calculation with decimals."""
        calc = Calculator()
        calc.perform_operation('10.5', '5.2', 'add')
        history = calc.get_history()
        assert '10.5' in str(history[0])
        assert 'add' in str(history[0])
    
    def test_clear_history_resets_memento(self):
        """Test that clear_history also resets memento stack."""
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        
        calc.clear_history()
        assert len(calc.get_history()) == 0
        assert not calc.can_undo()
        assert not calc.can_redo()
    
    def test_operation_case_insensitivity(self):
        """Test that operations are case insensitive."""
        calc = Calculator()
        result1 = calc.perform_operation('10', '5', 'ADD')
        
        calc2 = Calculator()
        result2 = calc2.perform_operation('10', '5', 'add')
        
        assert result1 == result2
    
    def test_simple_undo_redo(self):
        """Test simple undo and redo operations."""
        calc = Calculator()
        calc.perform_operation('10', '5', 'add')
        calc.perform_operation('15', '3', 'multiply')
        
        # Undo once
        result = calc.undo()
        assert result is not None
        assert result.operation == 'add'
        
        # Redo
        result = calc.redo()
        assert result is not None
        assert result.operation == 'multiply'
