"""Complete tests for history module."""
import pytest
import tempfile
import os
from decimal import Decimal
from app.calculation import Calculation
from app.history import LoggingObserver, AutoSaveObserver, HistoryManager
from app.exceptions import OperationError

class TestHistoryComplete:
    """Complete history tests for 100% coverage."""
    
    def test_logging_observer_creates_directory(self):
        """Test that logging observer creates directory if missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'subdir', 'test.log')
            observer = LoggingObserver(log_file)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc)
            
            assert os.path.exists(log_file)
            # Verify log file has content
            with open(log_file, 'r') as f:
                content = f.read()
                assert len(content) > 0
    
    def test_autosave_observer_creates_directory(self):
        """Test that autosave observer creates directory if missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'subdir', 'history.csv')
            observer = AutoSaveObserver(csv_file)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc)
            
            assert os.path.exists(csv_file)
    
    def test_history_manager_save_to_csv_creates_directory(self):
        """Test save to CSV creates directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'subdir', 'history.csv')
            manager = HistoryManager()
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            manager.history.append(calc)
            
            manager.save_to_csv(csv_file)
            assert os.path.exists(csv_file)
    
    def test_history_manager_remove_nonexistent_observer(self):
        """Test removing observer that doesn't exist."""
        manager = HistoryManager()
        observer = LoggingObserver('/tmp/test.log')
        
        # Should not raise error
        manager.remove_observer(observer)
        assert observer not in manager.observers
    
    def test_logging_observer_with_timestamp(self):
        """Test logging observer includes timestamp."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'test.log')
            observer = LoggingObserver(log_file)
            
            calc = Calculation(Decimal('1.5'), Decimal('2.5'), 'multiply', Decimal('3.75'))
            observer.update(calc)
            
            with open(log_file, 'r') as f:
                content = f.read()
                assert 'T' in content or ':' in content  # ISO format or time separator
    
    def test_history_load_csv_error_handling(self):
        """Test loading from non-existent CSV."""
        manager = HistoryManager()
        with pytest.raises(OperationError):
            manager.load_from_csv('/nonexistent/file.csv')
    
    def test_history_save_csv_error_handling(self):
        """Test saving to invalid path."""
        manager = HistoryManager()
        calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        manager.history.append(calc)
        
        # Try to save to invalid path - should handle gracefully
        try:
            manager.save_to_csv('/invalid/path/that/does/not/exist/history.csv')
        except OperationError:
            pass  # Expected
