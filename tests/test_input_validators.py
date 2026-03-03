"""Tests for input validators."""
import pytest
from decimal import Decimal
from app.input_validators import validate_decimal, validate_operation, validate_inputs
from app.exceptions import ValidationError

class TestValidateDecimal:
    """Test decimal validation."""
    
    def test_valid_decimal_string(self):
        """Test with valid decimal string."""
        result = validate_decimal('10.5')
        assert result == Decimal('10.5')
    
    def test_valid_integer_string(self):
        """Test with valid integer string."""
        result = validate_decimal('10')
        assert result == Decimal('10')
    
    def test_negative_number(self):
        """Test with negative number."""
        result = validate_decimal('-10.5')
        assert result == Decimal('-10.5')
    
    def test_empty_string_raises_error(self):
        """Test empty string raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_decimal('')
    
    def test_whitespace_only_raises_error(self):
        """Test whitespace only raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_decimal('   ')
    
    def test_invalid_string_raises_error(self):
        """Test invalid string raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_decimal('abc')
    
    def test_none_raises_error(self):
        """Test None raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_decimal(None)
    
    def test_whitespace_trimming(self):
        """Test whitespace is trimmed."""
        result = validate_decimal('  10.5  ')
        assert result == Decimal('10.5')

class TestValidateOperation:
    """Test operation validation."""
    
    def test_valid_operation(self):
        """Test valid operation."""
        result = validate_operation('add', ['add', 'subtract'])
        assert result == 'add'
    
    def test_case_insensitive(self):
        """Test case insensitivity."""
        result = validate_operation('ADD', ['add', 'subtract'])
        assert result == 'add'
    
    def test_whitespace_trimming(self):
        """Test whitespace trimming."""
        result = validate_operation('  add  ', ['add', 'subtract'])
        assert result == 'add'
    
    def test_invalid_operation_raises_error(self):
        """Test invalid operation raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_operation('invalid', ['add', 'subtract'])
    
    def test_empty_operation_raises_error(self):
        """Test empty operation raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_operation('', ['add', 'subtract'])

class TestValidateInputs:
    """Test multiple input validation."""
    
    def test_valid_inputs(self):
        """Test valid inputs."""
        a, b = validate_inputs('10', '5')
        assert a == Decimal('10')
        assert b == Decimal('5')
    
    def test_decimal_inputs(self):
        """Test decimal inputs."""
        a, b = validate_inputs('10.5', '5.2')
        assert a == Decimal('10.5')
        assert b == Decimal('5.2')
    
    def test_negative_inputs(self):
        """Test negative inputs."""
        a, b = validate_inputs('-10', '-5')
        assert a == Decimal('-10')
        assert b == Decimal('-5')
    
    def test_invalid_first_input_raises_error(self):
        """Test invalid first input raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_inputs('abc', '5')
    
    def test_invalid_second_input_raises_error(self):
        """Test invalid second input raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_inputs('10', 'abc')
