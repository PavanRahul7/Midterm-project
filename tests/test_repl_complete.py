"""Complete REPL tests for 100% coverage."""
import pytest
from io import StringIO
from unittest.mock import patch, MagicMock
from app.calculator_repl import CalculatorREPL

class TestREPLComplete:
    """Complete REPL tests for 100% coverage."""
    
    def test_repl_initialization(self):
        """Test REPL initialization."""
        repl = CalculatorREPL()
        assert repl.calculator is not None
    
    def test_repl_show_help(self):
        """Test REPL help command."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.show_help()
            assert mock_print.called
    
    def test_repl_show_history_empty(self):
        """Test REPL history with empty history."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.show_history()
            mock_print.assert_called_with("No history")
    
    def test_repl_show_history_with_entries(self):
        """Test REPL history with entries."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        with patch('builtins.print') as mock_print:
            repl.show_history()
            assert mock_print.called
    
    def test_repl_process_empty_command(self):
        """Test REPL with empty command."""
        repl = CalculatorREPL()
        repl.process_command('')
    
    def test_repl_process_whitespace_command(self):
        """Test REPL with whitespace command."""
        repl = CalculatorREPL()
        repl.process_command('   ')
    
    def test_repl_add_operation(self):
        """Test REPL add operation."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('add 10 5')
            assert mock_print.called
    
    def test_repl_invalid_operation_args(self):
        """Test REPL operation with wrong args."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('add 10')
            # Should print usage message
            assert mock_print.called
    
    def test_repl_unknown_command(self):
        """Test REPL unknown command."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('unknown_command')
            assert mock_print.called
    
    def test_repl_history_command(self):
        """Test REPL history command."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        with patch('builtins.print') as mock_print:
            repl.process_command('history')
            assert mock_print.called
    
    def test_repl_clear_command(self):
        """Test REPL clear command."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        with patch('builtins.print') as mock_print:
            repl.process_command('clear')
            assert mock_print.called
    
    def test_repl_undo_command(self):
        """Test REPL undo command."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        repl.calculator.perform_operation('15', '3', 'multiply')
        with patch('builtins.print') as mock_print:
            repl.process_command('undo')
            assert mock_print.called
    
    def test_repl_undo_nothing(self):
        """Test REPL undo when nothing to undo."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('undo')
            mock_print.assert_called_with("Nothing to undo")
    
    def test_repl_redo_command(self):
        """Test REPL redo command."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        repl.calculator.undo()
        with patch('builtins.print') as mock_print:
            repl.process_command('redo')
            assert mock_print.called
    
    def test_repl_redo_nothing(self):
        """Test REPL redo when nothing to redo."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('redo')
            mock_print.assert_called_with("Nothing to redo")
    
    def test_repl_save_command(self):
        """Test REPL save command."""
        repl = CalculatorREPL()
        repl.calculator.perform_operation('10', '5', 'add')
        with patch('builtins.print') as mock_print:
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as f:
                repl.process_command(f'save {f.name}')
                assert mock_print.called
    
    def test_repl_save_no_filename(self):
        """Test REPL save without filename."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('save')
            # Should show usage
            assert mock_print.called
    
    def test_repl_load_command(self):
        """Test REPL load command."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as f:
                # Create a CSV file
                repl.calculator.perform_operation('10', '5', 'add')
                repl.calculator.save_history(f.name)
                
                # Now load it
                repl2 = CalculatorREPL()
                repl2.process_command(f'load {f.name}')
                assert mock_print.called
    
    def test_repl_load_no_filename(self):
        """Test REPL load without filename."""
        repl = CalculatorREPL()
        with patch('builtins.print') as mock_print:
            repl.process_command('load')
            assert mock_print.called
    
    def test_repl_all_operations(self):
        """Test REPL with all operations."""
        repl = CalculatorREPL()
        ops = ['add', 'subtract', 'multiply', 'divide', 'power', 'root', 
               'modulus', 'int_divide', 'percent', 'abs_diff']
        
        for op in ops:
            with patch('builtins.print'):
                repl.process_command(f'{op} 10 5')
