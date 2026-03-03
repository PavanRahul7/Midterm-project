"""Main Calculator class (Facade pattern)."""
from decimal import Decimal
from typing import Optional, List
from app.calculation import Calculation
from app.operations import OperationFactory
from app.calculator_memento import CalculatorMemento, MementoCaretaker
from app.history import HistoryManager, LoggingObserver, AutoSaveObserver
from app.calculator_config import CalculatorConfig
from app.logger import Logger
from app.exceptions import OperationError, ValidationError
from app.input_validators import validate_inputs, validate_operation

class Calculator:
    """Main calculator class coordinating all subsystems."""
    
    def __init__(self):
        """Initialize calculator."""
        self.config = CalculatorConfig()
        self.logger = Logger()
        self.factory = OperationFactory()
        self.history_manager = HistoryManager()
        self.memento_caretaker = MementoCaretaker()
        self.last_calculation: Optional[Calculation] = None
        
        # Setup observers
        if self.config.auto_save:
            auto_save = AutoSaveObserver(self.config.history_file)
            self.history_manager.add_observer(auto_save)
        
        logging_observer = LoggingObserver(self.config.log_file)
        self.history_manager.add_observer(logging_observer)
        
        self.logger.info("Calculator initialized")
    
    def perform_operation(self, a_str: str, b_str: str, operation: str) -> Decimal:
        """Perform a calculation."""
        a, b = validate_inputs(a_str, b_str)
        validate_operation(operation, self.factory.get_available_operations())
        
        op = self.factory.get_operation(operation)
        result = op.execute(a, b)
        
        # Check precision
        result_str = str(result)
        if '.' in result_str:
            decimal_places = len(result_str.split('.')[-1])
            if decimal_places > self.config.precision:
                result = result.quantize(Decimal(10) ** -self.config.precision)
        
        # Create and save calculation
        calculation = Calculation(a, b, operation, result)
        self.last_calculation = calculation
        
        # Save memento
        memento = CalculatorMemento(a, b, operation, result)
        self.memento_caretaker.save(memento)
        
        # Notify observers
        self.history_manager.notify_observers(calculation)
        self.logger.info(f"Operation: {calculation}")
        
        return result
    
    def undo(self) -> Optional[Calculation]:
        """Undo last operation."""
        memento = self.memento_caretaker.undo()
        if memento:
            self.last_calculation = Calculation(memento.a, memento.b, memento.operation, memento.result)
            self.logger.info(f"Undo: {self.last_calculation}")
            return self.last_calculation
        return None
    
    def redo(self) -> Optional[Calculation]:
        """Redo last undone operation."""
        memento = self.memento_caretaker.redo()
        if memento:
            self.last_calculation = Calculation(memento.a, memento.b, memento.operation, memento.result)
            self.logger.info(f"Redo: {self.last_calculation}")
            return self.last_calculation
        return None
    
    def can_undo(self) -> bool:
        """Check if undo is available."""
        return self.memento_caretaker.can_undo()
    
    def can_redo(self) -> bool:
        """Check if redo is available."""
        return self.memento_caretaker.can_redo()
    
    def get_history(self) -> List[Calculation]:
        """Get calculation history."""
        return self.history_manager.get_history()
    
    def clear_history(self) -> None:
        """Clear history."""
        self.history_manager.clear_history()
        self.memento_caretaker.clear()
        self.logger.info("History cleared")
    
    def save_history(self, filepath: str) -> None:
        """Save history to CSV."""
        self.history_manager.save_to_csv(filepath)
        self.logger.info(f"History saved to {filepath}")
    
    def load_history(self, filepath: str) -> None:
        """Load history from CSV."""
        self.history_manager.load_from_csv(filepath)
        self.logger.info(f"History loaded from {filepath}")
    
    def get_available_operations(self) -> list:
        """Get available operations."""
        return self.factory.get_available_operations()
