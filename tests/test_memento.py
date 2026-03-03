"""Tests for Memento pattern."""
import pytest
from decimal import Decimal
from app.calculator_memento import CalculatorMemento, MementoCaretaker

class TestCalculatorMemento:
    """Test CalculatorMemento."""
    
    def test_memento_creation(self):
        memento = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        assert memento.a == Decimal('10')
        assert memento.b == Decimal('5')
        assert memento.operation == 'add'
        assert memento.result == Decimal('15')

class TestMementoCaretaker:
    """Test MementoCaretaker for undo/redo."""
    
    def test_save_operation(self):
        caretaker = MementoCaretaker()
        memento = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(memento)
        assert len(caretaker.undo_stack) == 1
    
    def test_undo_operation(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        m2 = CalculatorMemento(Decimal('15'), Decimal('3'), 'multiply', Decimal('45'))
        caretaker.save(m1)
        caretaker.save(m2)
        
        result = caretaker.undo()
        assert result.result == Decimal('15')
        assert len(caretaker.undo_stack) == 1
        assert len(caretaker.redo_stack) == 1
    
    def test_redo_operation(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        m2 = CalculatorMemento(Decimal('15'), Decimal('3'), 'multiply', Decimal('45'))
        caretaker.save(m1)
        caretaker.save(m2)
        
        caretaker.undo()
        result = caretaker.redo()
        assert result.result == Decimal('45')
        assert len(caretaker.undo_stack) == 2
        assert len(caretaker.redo_stack) == 0
    
    def test_cannot_undo_with_single_state(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(m1)
        
        result = caretaker.undo()
        assert result is None
    
    def test_cannot_redo_with_empty_redo_stack(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(m1)
        
        result = caretaker.redo()
        assert result is None
    
    def test_can_undo_true(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        m2 = CalculatorMemento(Decimal('15'), Decimal('3'), 'multiply', Decimal('45'))
        caretaker.save(m1)
        caretaker.save(m2)
        assert caretaker.can_undo() is True
    
    def test_can_undo_false(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(m1)
        assert caretaker.can_undo() is False
    
    def test_can_redo_true(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        m2 = CalculatorMemento(Decimal('15'), Decimal('3'), 'multiply', Decimal('45'))
        caretaker.save(m1)
        caretaker.save(m2)
        caretaker.undo()
        assert caretaker.can_redo() is True
    
    def test_can_redo_false(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(m1)
        assert caretaker.can_redo() is False
    
    def test_clear_stacks(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        caretaker.save(m1)
        caretaker.clear()
        assert len(caretaker.undo_stack) == 0
        assert len(caretaker.redo_stack) == 0
    
    def test_redo_clears_redo_stack_on_new_save(self):
        caretaker = MementoCaretaker()
        m1 = CalculatorMemento(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
        m2 = CalculatorMemento(Decimal('15'), Decimal('3'), 'multiply', Decimal('45'))
        m3 = CalculatorMemento(Decimal('45'), Decimal('2'), 'divide', Decimal('22.5'))
        
        caretaker.save(m1)
        caretaker.save(m2)
        caretaker.undo()
        assert caretaker.can_redo() is True
        
        caretaker.save(m3)
        assert caretaker.can_redo() is False
