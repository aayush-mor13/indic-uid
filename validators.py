from .character_sets import get_character_pool

def is_valid_id(id_string, scripts=None, length=None):
    """
    Validate if a string is a valid Indic ID.
    
    Args:
        id_string: The ID string to validate
        scripts: Expected scripts (None means any script is valid)
        length: Expected length (None means any length is valid)
    
    Returns:
        bool: True if valid, False otherwise
    """
    if not id_string:
        return False
    
    if length is not None and len(id_string) != length:
        return False
    
    valid_chars = set(get_character_pool(scripts))
    
    return all(char in valid_chars for char in id_string)


def get_script_of_char(char):
    """
    Identify which script a character belongs to.
    
    Args:
        char: A single character
    
    Returns:
        str or None: Script name if found, None otherwise
    """
    from .character_sets import SCRIPTS
    
    for script_name, script_data in SCRIPTS.items():
        if char in script_data['all']:
            return script_name
    
    return None

