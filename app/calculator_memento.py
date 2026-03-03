"""Memento pattern for undo/redo functionality."""
from decimal import Decimal
from typing import List, Optional

class CalculatorMemento:
    """Captures calculator state."""
    
    def __init__(self, a: Decimal, b: Decimal, operation: str, result: Decimal):
        """Initialize memento."""
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

class MementoCaretaker:
    """Manages undo/redo stacks."""
    
    def __init__(self):
        """Initialize caretaker."""
        self.undo_stack: List[CalculatorMemento] = []
        self.redo_stack: List[CalculatorMemento] = []
    
    def save(self, memento: CalculatorMemento) -> None:
        """Save state to undo stack."""
        self.undo_stack.append(memento)
        self.redo_stack.clear()
    
    def undo(self) -> Optional[CalculatorMemento]:
        """Undo last operation."""
        if len(self.undo_stack) < 2:
            return None
        
        current = self.undo_stack.pop()
        self.redo_stack.append(current)
        return self.undo_stack[-1]
    
    def redo(self) -> Optional[CalculatorMemento]:
        """Redo last undone operation."""
        if not self.redo_stack:
            return None
        
        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento
    
    def can_undo(self) -> bool:
        """Check if undo is available."""
        return len(self.undo_stack) >= 2
    
    def can_redo(self) -> bool:
        """Check if redo is available."""
        return len(self.redo_stack) > 0
    
    def clear(self) -> None:
        """Clear all stacks."""
        self.undo_stack.clear()
        self.redo_stack.clear()
