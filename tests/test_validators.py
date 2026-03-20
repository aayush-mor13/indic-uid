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
    script = get_script_of_char('!')
    assert script is None


def test_is_valid_id_with_numbers():
    """Test validation of IDs that contain numbers."""
    id = generate_id(length=6, scripts=['devanagari'], include_numbers=True)
    assert is_valid_id(id, scripts=['devanagari'], include_numbers=True) is True


def test_is_valid_id_number_chars_invalid_without_flag():
    """Test that number-only string is invalid without include_numbers."""
    assert is_valid_id('\u0966\u0967\u0968\u0969\u096a\u096b') is False


def test_is_valid_id_number_chars_valid_with_flag():
    """Test that number-only string is valid with include_numbers."""
    assert is_valid_id('\u0966\u0967\u0968\u0969\u096a\u096b', scripts=['devanagari'], include_numbers=True) is True


def test_get_script_of_number_char():
    """Test script detection for a number character."""
    script = get_script_of_char('\u0967')  # Devanagari 1
    assert script == 'devanagari'
