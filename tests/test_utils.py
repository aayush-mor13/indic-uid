import pytest
from indic_uid import calculate_collision_probability, estimate_safe_id_count


def test_calculate_collision_probability():
    """Test collision probability calculation."""
    prob = calculate_collision_probability(num_ids=1000, length=6, num_scripts=6)
    assert 0 <= prob <= 1
    assert prob < 0.01  # Should be very low for 1000 IDs


def test_estimate_safe_id_count():
    """Test safe ID count estimation."""
    count = estimate_safe_id_count(length=6, num_scripts=6)
    assert count > 0
    assert isinstance(count, int)

