"""Observer pattern for history management."""
from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from pathlib import Path
from decimal import Decimal
import pandas as pd
from app.calculation import Calculation
from app.exceptions import OperationError

class Observer(ABC):
    """Abstract observer for calculations."""
    
    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        """Update observer with new calculation."""
        pass

class LoggingObserver(Observer):
    """Observer that logs calculations."""
    
    def __init__(self, log_file: str):
        """Initialize logging observer."""
        self.log_file = log_file
    
    def update(self, calculation: Calculation) -> None:
        """Log calculation."""
        Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_file, 'a') as f:
            timestamp = datetime.now().isoformat()
            f.write(f"{timestamp} | {calculation}\n")

class AutoSaveObserver(Observer):
    """Observer that auto-saves to CSV."""
    
    def __init__(self, csv_file: str):
        """Initialize auto-save observer."""
        self.csv_file = csv_file
    
    def update(self, calculation: Calculation) -> None:
        """Save calculation to CSV."""
        try:
            Path(self.csv_file).parent.mkdir(parents=True, exist_ok=True)
            data = [calculation.to_dict()]
            df = pd.DataFrame(data)
            
            if Path(self.csv_file).exists():
                existing_df = pd.read_csv(self.csv_file)
                df = pd.concat([existing_df, df], ignore_index=True)
            
            df.to_csv(self.csv_file, index=False)
        except Exception as e:
            raise OperationError(f"Failed to save: {e}")

class HistoryManager:
    """Manages calculation history and observers."""
    
    def __init__(self):
        """Initialize history manager."""
        self.history: List[Calculation] = []
        self.observers: List[Observer] = []
    
    def add_observer(self, observer: Observer) -> None:
        """Add observer."""
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer) -> None:
        """Remove observer."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self, calculation: Calculation) -> None:
        """Notify all observers."""
        self.history.append(calculation)
        for observer in self.observers:
            observer.update(calculation)
    
    def get_history(self) -> List[Calculation]:
        """Get all calculations."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear history."""
        self.history.clear()
    
    def load_from_csv(self, csv_file: str) -> None:
        """Load history from CSV."""
        try:
            df = pd.read_csv(csv_file)
            for _, row in df.iterrows():
                self.history.append(Calculation.from_dict(row.to_dict()))
        except Exception as e:
            raise OperationError(f"Failed to load: {e}")
    
    def save_to_csv(self, csv_file: str) -> None:
        """Save history to CSV."""
        try:
            Path(csv_file).parent.mkdir(parents=True, exist_ok=True)
            data = [calc.to_dict() for calc in self.history]
            df = pd.DataFrame(data)
            df.to_csv(csv_file, index=False)
        except Exception as e:
            raise OperationError(f"Failed to save: {e}")
