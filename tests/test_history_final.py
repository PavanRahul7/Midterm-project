"""Final history tests for 100% coverage."""
import pytest
import tempfile
import os
from decimal import Decimal
from pathlib import Path
from app.calculation import Calculation
from app.history import LoggingObserver, AutoSaveObserver, HistoryManager
from app.exceptions import OperationError

class TestHistoryFinal:
    """Final history tests for 100% coverage."""
    
    def test_logging_observer_appends(self):
        """Test logging observer appends to file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'test.log')
            observer = LoggingObserver(log_file)
            
            calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            calc2 = Calculation(Decimal('20'), Decimal('3'), 'multiply', Decimal('60'))
            
            observer.update(calc1)
            observer.update(calc2)
            
            with open(log_file, 'r') as f:
                lines = f.readlines()
                assert len(lines) == 2
    
    def test_autosave_with_existing_csv(self):
        """Test autosave appends to existing CSV."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'history.csv')
            observer = AutoSaveObserver(csv_file)
            
            # First write
            calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc1)
            
            # Second write
            calc2 = Calculation(Decimal('20'), Decimal('3'), 'multiply', Decimal('60'))
            observer.update(calc2)
            
            # Verify both are in file
            import pandas as pd
            df = pd.read_csv(csv_file)
            assert len(df) == 2
    
    def test_history_manager_get_history_copy(self):
        """Test get_history returns a copy."""
        manager = HistoryManager()
        calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        manager.history.append(calc1)
        
        history1 = manager.get_history()
        history2 = manager.get_history()
        
        # They should be equal but not the same object
        assert history1 == history2
        assert history1 is not history2
    
    def test_history_manager_multiple_observers(self):
        """Test history manager with multiple observers."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'test.log')
            csv_file = os.path.join(tmpdir, 'history.csv')
            
            manager = HistoryManager()
            log_observer = LoggingObserver(log_file)
            csv_observer = AutoSaveObserver(csv_file)
            
            manager.add_observer(log_observer)
            manager.add_observer(csv_observer)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            manager.notify_observers(calc)
            
            # Both should have recorded the event
            assert os.path.exists(log_file)
            assert os.path.exists(csv_file)
    
    def test_history_manager_operations_path(self):
        """Test history operations with valid path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'nested', 'dir', 'history.csv')
            manager = HistoryManager()
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            manager.history.append(calc)
            
            # Should create nested directories
            manager.save_to_csv(csv_file)
            assert os.path.exists(csv_file)
