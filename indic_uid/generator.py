import secrets
from .character_sets import get_character_pool

DEFAULT_LENGTH = 6


def generate_id(length=DEFAULT_LENGTH, scripts=None, pronounceable=False):
    """
    Generate a unique ID using Indian script characters.
    
    Args:
        length: Length of the ID (default: 6)
        scripts: List of scripts to use. Options: 'devanagari', 'gujarati', 
                'kannada', 'tamil', 'telugu', 'bengali'. If None, uses all.
        pronounceable: If True, alternates between vowels and consonants for 
                      better pronunciation (slightly reduces entropy)
    
    Returns:
        str: Generated unique ID
        
    Examples:
        >>> generate_id()
        'कஆಗઘతअ'
        
        >>> generate_id(length=5, scripts=['devanagari'])
        'घअकआइ'
        
        >>> generate_id(pronounceable=True, scripts=['devanagari'])
        'कअखइगउ'
    """
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    if pronounceable:
        vowels, consonants = get_character_pool(scripts, pronounceable=True)
        
        if not vowels or not consonants:
            raise ValueError("Not enough vowels or consonants in selected scripts")
        
        # Alternate consonant-vowel for pronounceability
        id_chars = []
        for i in range(length):
            if i % 2 == 0:
                id_chars.append(secrets.choice(consonants))
            else:
                id_chars.append(secrets.choice(vowels))
        
        return ''.join(id_chars)
    else:
        chars = get_character_pool(scripts, pronounceable=False)
        
        if not chars:
            raise ValueError("No characters available for selected scripts")
        
        # Pure random selection
        return ''.join(secrets.choice(chars) for _ in range(length))


def generate_batch(count, length=DEFAULT_LENGTH, scripts=None, pronounceable=False):
    """
    Generate multiple IDs at once.
    
    Args:
        count: Number of IDs to generate
        length: Length of each ID
        scripts: List of scripts to use
        pronounceable: Whether to generate pronounceable IDs
    
    Returns:
        list: List of generated IDs
    """
    return [generate_id(length, scripts, pronounceable) for _ in range(count)]
