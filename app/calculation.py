"""Calculation model representing a single calculation."""
from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, Any

@dataclass
class Calculation:
    """Represents a single calculation with operands, operation, and result."""
    
    a: Decimal
    b: Decimal
    operation: str
    result: Decimal
    
    def __post_init__(self):
        """Validate calculation data."""
        if not isinstance(self.a, Decimal):
            self.a = Decimal(str(self.a))
        if not isinstance(self.b, Decimal):
            self.b = Decimal(str(self.b))
        if not isinstance(self.result, Decimal):
            self.result = Decimal(str(self.result))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'a': str(self.a),
            'b': str(self.b),
            'operation': self.operation,
            'result': str(self.result)
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Calculation':
        """Create from dictionary."""
        return cls(
            a=Decimal(str(data['a'])),
            b=Decimal(str(data['b'])),
            operation=data['operation'],
            result=Decimal(str(data['result']))
        )
    
    def __str__(self) -> str:
        """String representation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"
