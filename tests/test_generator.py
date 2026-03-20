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


def test_generate_id_with_numbers():
    """Test ID generation with numbers included."""
    id = generate_id(length=8, scripts=['devanagari'], include_numbers=True)
    assert len(id) == 8
    assert isinstance(id, str)


def test_generate_id_numbers_only_pool():
    """Test that include_numbers adds number chars to the pool."""
    from indic_uid.character_sets import SCRIPTS
    # Generate many IDs and check at least one contains a number char
    number_chars = set(SCRIPTS['devanagari']['numbers'])
    ids = generate_batch(100, length=10, scripts=['devanagari'], include_numbers=True)
    all_chars = set(''.join(ids))
    assert all_chars & number_chars, "Expected at least one number character in 100 IDs"


def test_generate_id_without_numbers_has_no_digits():
    """Test that without include_numbers, no number chars appear."""
    from indic_uid.character_sets import SCRIPTS
    number_chars = set(SCRIPTS['devanagari']['numbers'])
    ids = generate_batch(100, length=10, scripts=['devanagari'], include_numbers=False)
    all_chars = set(''.join(ids))
    assert not (all_chars & number_chars), "No number chars expected without include_numbers"


def test_generate_batch_with_numbers():
    """Test batch generation with numbers."""
    ids = generate_batch(10, length=6, include_numbers=True)
    assert len(ids) == 10
    assert all(len(id) == 6 for id in ids)


def test_generate_id_numbers_only():
    """Test numbers-only OTP generation."""
    from indic_uid.character_sets import SCRIPTS
    number_chars = set(SCRIPTS['devanagari']['numbers'])
    id = generate_id(length=6, scripts=['devanagari'], numbers_only=True)
    assert len(id) == 6
    assert all(char in number_chars for char in id)


def test_generate_id_numbers_only_multi_script():
    """Test numbers-only with multiple scripts."""
    from indic_uid.character_sets import SCRIPTS
    valid = set(SCRIPTS['devanagari']['numbers']) | set(SCRIPTS['tamil']['numbers'])
    id = generate_id(length=8, scripts=['devanagari', 'tamil'], numbers_only=True)
    assert len(id) == 8
    assert all(char in valid for char in id)


def test_generate_batch_numbers_only():
    """Test batch generation with numbers_only."""
    from indic_uid.character_sets import SCRIPTS
    number_chars = set(SCRIPTS['devanagari']['numbers'])
    ids = generate_batch(10, length=6, scripts=['devanagari'], numbers_only=True)
    assert len(ids) == 10
    for id in ids:
        assert all(char in number_chars for char in id)

