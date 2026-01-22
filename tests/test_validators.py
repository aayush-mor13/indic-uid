import pytest
from indic_uid import generate_id, is_valid_id, get_script_of_char


def test_is_valid_id():
    """Test ID validation."""
    id = generate_id()
    assert is_valid_id(id) is True


def test_is_valid_id_wrong_length():
    """Test validation with wrong length."""
    id = generate_id(length=5)
    assert is_valid_id(id, length=6) is False


def test_is_valid_id_invalid_chars():
    """Test validation with invalid characters."""
    assert is_valid_id('abc123') is False


def test_get_script_of_char():
    """Test script detection."""
    id = generate_id(length=1, scripts=['devanagari'])
    script = get_script_of_char(id)
    assert script == 'devanagari'


def test_get_script_of_char_invalid():
    """Test script detection with invalid character."""
    script = get_script_of_char('1')
    assert script is None
