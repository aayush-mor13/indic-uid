"""
Indic IDs - Generate unique IDs using Indian script characters.

A simple library for generating short, unique identifiers using characters
from various Indian language scripts (Devanagari, Gujarati, Kannada, etc.).
"""

from .generator import generate_id, generate_batch
from .validators import is_valid_id, get_script_of_char
from .character_sets import get_available_scripts
from .utils import calculate_collision_probability, estimate_safe_id_count

__version__ = '0.2.0'
__all__ = [
    'generate_id',
    'generate_batch',
    'is_valid_id',
    'get_script_of_char',
    'get_available_scripts',
    'calculate_collision_probability',
    'estimate_safe_id_count'
]
