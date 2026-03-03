"""Input validation functions."""
from decimal import Decimal, InvalidOperation
from typing import Tuple
from app.exceptions import ValidationError

def validate_decimal(value: str) -> Decimal:
    """Validate and convert to Decimal."""
    if not value or not str(value).strip():
        raise ValidationError("Input cannot be empty")
    
    try:
        return Decimal(str(value).strip())
    except (InvalidOperation, ValueError, TypeError):
        raise ValidationError(f"Invalid number: {value}")

def validate_operation(operation: str, available: list) -> str:
    """Validate operation name."""
    if not operation:
        raise ValidationError("Operation cannot be empty")
    
    op_lower = operation.lower().strip()
    if op_lower not in available:
        raise ValidationError(f"Unknown operation: {operation}")
    
    return op_lower

def validate_inputs(a: str, b: str) -> Tuple[Decimal, Decimal]:
    """Validate two inputs."""
    return validate_decimal(a), validate_decimal(b)
