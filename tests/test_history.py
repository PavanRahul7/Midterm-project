"""Tests for History and Observer patterns."""
import pytest
import os
import tempfile
from decimal import Decimal
from app.calculation import Calculation
from app.history import Observer, LoggingObserver, AutoSaveObserver, HistoryManager
from app.exceptions import OperationError

class TestLogObserver:
    """Test LoggingObserver."""
    
    def test_logging_observer_writes_log(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'test.log')
            observer = LoggingObserver(log_file)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc)
            
            assert os.path.exists(log_file)
            with open(log_file, 'r') as f:
                content = f.read()
                assert 'add' in content

class TestAutoSaveObserver:
    """Test AutoSaveObserver."""
    
    def test_autosave_creates_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'test.csv')
            observer = AutoSaveObserver(csv_file)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc)
            
            assert os.path.exists(csv_file)
    
    def test_autosave_appends_to_existing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'test.csv')
            observer = AutoSaveObserver(csv_file)
            
            calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            observer.update(calc1)
            
            calc2 = Calculation(Decimal('20'), Decimal('5'), 'multiply', Decimal('100'))
            observer.update(calc2)
            
            import pandas as pd
            df = pd.read_csv(csv_file)
            assert len(df) == 2

class TestHistoryManager:
    """Test HistoryManager."""
    
    def test_add_observer(self):
        manager = HistoryManager()
        observer = LoggingObserver('/tmp/test.log')
        manager.add_observer(observer)
        assert observer in manager.observers
    
    def test_remove_observer(self):
        manager = HistoryManager()
        observer = LoggingObserver('/tmp/test.log')
        manager.add_observer(observer)
        manager.remove_observer(observer)
        assert observer not in manager.observers
    
    def test_notify_observers(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, 'test.log')
            manager = HistoryManager()
            observer = LoggingObserver(log_file)
            manager.add_observer(observer)
            
            calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            manager.notify_observers(calc)
            
            assert len(manager.history) == 1
            assert os.path.exists(log_file)
    
    def test_get_history(self):
        manager = HistoryManager()
        calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        calc2 = Calculation(Decimal('20'), Decimal('5'), 'multiply', Decimal('100'))
        
        manager.history.append(calc1)
        manager.history.append(calc2)
        
        history = manager.get_history()
        assert len(history) == 2
        assert history[0] == calc1
    
    def test_clear_history(self):
        manager = HistoryManager()
        calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        manager.history.append(calc)
        
        manager.clear_history()
        assert len(manager.history) == 0
    
    def test_save_to_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'history.csv')
            manager = HistoryManager()
            
            calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            calc2 = Calculation(Decimal('20'), Decimal('5'), 'multiply', Decimal('100'))
            manager.history.append(calc1)
            manager.history.append(calc2)
            
            manager.save_to_csv(csv_file)
            assert os.path.exists(csv_file)
    
    def test_load_from_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_file = os.path.join(tmpdir, 'history.csv')
            
            # Create CSV
            manager1 = HistoryManager()
            calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
            manager1.history.append(calc1)
            manager1.save_to_csv(csv_file)
            
            # Load CSV
            manager2 = HistoryManager()
            manager2.load_from_csv(csv_file)
            assert len(manager2.history) == 1
