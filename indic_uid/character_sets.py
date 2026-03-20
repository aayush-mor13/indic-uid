"""
Character sets for various Indian scripts.
Characters are carefully selected to avoid visual similarity.
"""

SCRIPTS = {
    'devanagari': {
        'vowels': ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ'],
        'consonants': ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 
                      'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 
                      'व', 'श', 'ष', 'स', 'ह'],
        'numbers': ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'],
        'all': ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'क', 'ख', 'ग', 'घ', 
               'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 
               'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह']
    },
    'gujarati': {
        'vowels': ['અ', 'આ', 'ઇ', 'ઈ', 'உ', 'ઊ', 'એ', 'ઐ', 'ઓ', 'ઔ'],
        'consonants': ['ક', 'ખ', 'ગ', 'ઘ', 'ચ', 'છ', 'જ', 'ઝ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ',
                      'ત', 'થ', 'દ', 'ધ', 'ન', 'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ',
                      'વ', 'શ', 'ષ', 'સ', 'હ'],
        'numbers': ['૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯'],
        'all': ['અ', 'આ', 'ઇ', 'ઈ', 'உ', 'ઊ', 'એ', 'ઐ', 'ઓ', 'ઔ', 'ક', 'ખ', 'ગ', 'ઘ',
               'ચ', 'છ', 'જ', 'ઝ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'થ', 'દ', 'ધ', 'ન',
               'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'વ', 'શ', 'ષ', 'સ', 'હ']
    },
    'kannada': {
        'vowels': ['ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ', 'ಎ', 'ಏ', 'ಐ', 'ಒ', 'ಓ', 'ಔ'],
        'consonants': ['ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ',
                      'ತ', 'ಥ', 'ದ', 'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಲ',
                      'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ'],
        'numbers': ['೦', '೧', '೨', '೩', '೪', '೫', '೬', '೭', '೮', '೯'],
        'all': ['ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ', 'ಎ', 'ಏ', 'ಐ', 'ಒ', 'ಓ', 'ಔ', 'ಕ', 'ಖ',
               'ಗ', 'ಘ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ', 'ತ', 'ಥ', 'ದ',
               'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ',
               'ಹ', 'ಳ']
    },
    'tamil': {
        'vowels': ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ'],
        'consonants': ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர',
                      'ல', 'வ', 'ழ', 'ள', 'ற', 'ன'],
        'numbers': ['௦', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯'],
        'all': ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ', 'க',
               'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ',
               'ழ', 'ள', 'ற', 'ன']
    },
    'telugu': {
        'vowels': ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ'],
        'consonants': ['క', 'ఖ', 'గ', 'ఘ', 'చ', 'ఛ', 'జ', 'ఝ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
                      'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల',
                      'వ', 'శ', 'ష', 'స', 'హ', 'ళ'],
        'numbers': ['౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯'],
        'all': ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ', 'క', 'ఖ',
               'గ', 'ఘ', 'చ', 'ఛ', 'జ', 'ఝ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ', 'త', 'థ', 'ద',
               'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ', 'శ', 'ష', 'స',
               'హ', 'ళ']
    },
    'bengali': {
        'vowels': ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'এ', 'ঐ', 'ও', 'ঔ'],
        'consonants': ['ক', 'খ', 'গ', 'ঘ', 'চ', 'ছ', 'জ', 'ঝ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ',
                      'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল',
                      'শ', 'ষ', 'স', 'হ'],
        'numbers': ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'],
        'all': ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'এ', 'ঐ', 'ও', 'ঔ', 'ক', 'খ', 'গ', 'ঘ',
               'চ', 'ছ', 'জ', 'ঝ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন',
               'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ']
    },
    'english': {
        'vowels': ['a', 'e', 'i', 'o', 'u'],
        'consonants': [
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        ],
        'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'all': [
            'a', 'e', 'i', 'o', 'u',
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        ]
    }
}

def get_available_scripts():
    """Return list of available script names."""
    return list(SCRIPTS.keys())

def get_character_pool(scripts=None, pronounceable=False, include_numbers=False, numbers_only=False):
    """
    Get combined character pool from specified scripts.
    
    Args:
        scripts: List of script names. If None, uses all scripts.
        pronounceable: If True, returns separate vowel and consonant pools.
        include_numbers: If True, includes number characters in the pool.
        numbers_only: If True, returns only number characters.
    
    Returns:
        If pronounceable=False: List of characters
        If pronounceable=True: Tuple of (vowels, consonants)
    """
    if scripts is None:
        scripts = get_available_scripts()

    # Validate scripts
    invalid_scripts = set(scripts) - set(SCRIPTS.keys())
    if invalid_scripts:
        raise ValueError(f"Invalid scripts: {invalid_scripts}. Available: {get_available_scripts()}")
    
    if numbers_only:
        chars = []
        for script in scripts:
            chars.extend(SCRIPTS[script]['numbers'])
        return chars
    
    if pronounceable:
        vowels = []
        consonants = []
        for script in scripts:
            vowels.extend(SCRIPTS[script]['vowels'])
            consonants.extend(SCRIPTS[script]['consonants'])
        return vowels, consonants
    else:
        chars = []
        for script in scripts:
            chars.extend(SCRIPTS[script]['all'])
            if include_numbers:
                chars.extend(SCRIPTS[script]['numbers'])
        return chars
