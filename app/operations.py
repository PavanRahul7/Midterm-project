"""Operation implementations with Factory pattern."""
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from typing import Dict, Type
from app.exceptions import OperationError

class Operation(ABC):
    """Abstract operation class."""
    
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Execute operation."""
        pass

class Add(Operation):
    """Addition operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

class Subtract(Operation):
    """Subtraction operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a - b

class Multiply(Operation):
    """Multiplication operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

class Divide(Operation):
    """Division operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise OperationError("Division by zero")
        return a / b

class Power(Operation):
    """Power operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        try:
            return a ** b
        except (ValueError, OverflowError) as e:
            raise OperationError(f"Power calculation failed: {e}")

class Root(Operation):
    """Root operation (nth root)."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise OperationError("Root index cannot be zero")
        # Determine if b is an integer index
        try:
            b_int = int(b)
            b_is_int = (Decimal(b_int) == b)
        except (ValueError, OverflowError):
            b_is_int = False

        # Disallow even root of negative numbers
        if a < 0 and b_is_int and b_int % 2 == 0:
            raise OperationError("Cannot take even root of negative number")

        exponent = Decimal(1) / b
        try:
            if a < 0:
                # Negative base with odd integer index -> negative result
                if b_is_int and b_int % 2 == 1:
                    return -(abs(a) ** exponent)
                # If exponent is an integer (e.g., b == 0.5 -> exponent == 2), allow integer exponentiation
                if exponent == exponent.to_integral_value():
                    return a ** exponent
                # Otherwise it's a non-integer root of a negative number -> not supported
                raise OperationError("Cannot take non-integer root of negative number")
            return a ** exponent
        except (ValueError, OverflowError, InvalidOperation) as e:
            raise OperationError(f"Root calculation failed: {e}")

class Modulus(Operation):
    """Modulus operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise OperationError("Cannot modulo by zero")
        return a % b

class IntDivide(Operation):
    """Integer division operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise OperationError("Division by zero")
        return Decimal(int(a) // int(b))

class Percentage(Operation):
    """Percentage operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero divisor")
        return (a / b) * 100

class AbsDiff(Operation):
    """Absolute difference operation."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return abs(a - b)

class OperationFactory:
    """Factory for creating operations."""
    
    _operations: Dict[str, Type[Operation]] = {
        'add': Add,
        'subtract': Subtract,
        'multiply': Multiply,
        'divide': Divide,
        'power': Power,
        'root': Root,
        'modulus': Modulus,
        'int_divide': IntDivide,
        'percent': Percentage,
        'abs_diff': AbsDiff,
    }
    
    @classmethod
    def get_operation(cls, name: str) -> Operation:
        """Get operation by name."""
        op_class = cls._operations.get(name.lower())
        if not op_class:
            raise OperationError(f"Unknown operation: {name}")
        return op_class()
    
    @classmethod
    def get_available_operations(cls) -> list:
        """Get list of available operations."""
        return sorted(cls._operations.keys())
