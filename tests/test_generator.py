import pytest
from indic_uid import generate_id, generate_batch


def test_generate_id_default():
    """Test default ID generation."""
    id = generate_id()
    assert len(id) == 6
    assert isinstance(id, str)


def test_generate_id_custom_length():
    """Test custom length generation."""
    id = generate_id(length=10)
    assert len(id) == 10


def test_generate_id_specific_script():
    """Test generation with specific script."""
    id = generate_id(scripts=['devanagari'])
    assert len(id) == 6


def test_generate_id_pronounceable():
    """Test pronounceable ID generation."""
    id = generate_id(pronounceable=True, scripts=['devanagari'])
    assert len(id) == 6


def test_generate_id_invalid_length():
    """Test that invalid length raises error."""
    with pytest.raises(ValueError):
        generate_id(length=0)


def test_generate_id_invalid_script():
    """Test that invalid script raises error."""
    with pytest.raises(ValueError):
        generate_id(scripts=['invalid_script'])


def test_generate_batch():
    """Test batch generation."""
    ids = generate_batch(10, length=5)
    assert len(ids) == 10
    assert all(len(id) == 5 for id in ids)


def test_generate_id_uniqueness():
    """Test that generated IDs are unique (probabilistically)."""
    ids = generate_batch(1000)
    assert len(ids) == len(set(ids))  # All should be unique

