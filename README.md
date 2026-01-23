# Indic UID

[![PyPI version](https://badge.fury.io/py/indic-uid.svg)](https://badge.fury.io/py/indic-uid)
[![Python Versions](https://img.shields.io/pypi/pyversions/indic-uid.svg)](https://pypi.org/project/indic-uid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
Generate short, unique identifiers using characters from Indian language scripts (Devanagari, Gujarati, Kannada, Tamil, Telugu, Bengali) and English.

Perfect for referral codes, short URLs, or any system requiring unique identifiers with an Indian language touch!

## ✨ Features

- 🎯 **Multiple Scripts**: Support for 7 Indian scripts (Devanagari, Gujarati, Kannada, Tamil, Telugu, Bengali, English)
- 🔐 **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- 🎲 **Flexible Generation**: Choose between pure random or pronounceable IDs
- ✅ **Validation Built-in**: Validate IDs and detect their script
- 📊 **Collision Analysis**: Calculate probability of ID collisions
- 🚀 **Zero Dependencies**: Lightweight, no external dependencies
- 🎨 **Simple API**: Easy to use, intuitive interface

## 📦 Installation

```bash
pip install indic-uid
```

**Note**

The package is installed as `indic-uid`, but imported in Python as `indic_uid`


## 🚀 Quick Start

```python
from indic_uid import generate_id

# Generate a random 6-character ID
id = generate_id()
print(id)  # Example: 'कஆಗઘతঅ'

# Generate with specific length
id = generate_id(length=8)
print(id)  # Example: 'अкஆগઘతaక'

# Generate from specific script
id = generate_id(scripts=['devanagari'])
print(id)  # Example: 'घअकआइश'

# Generate pronounceable IDs (alternates vowels and consonants)
id = generate_id(pronounceable=True, scripts=['devanagari'])
print(id)  # Example: 'कअखइगउ'
```

## 📖 Usage Examples

### Basic ID Generation

```python
from indic_uid import generate_id, generate_batch

# Default: 6 characters, all scripts
id = generate_id()

# Custom length
short_id = generate_id(length=4)
long_id = generate_id(length=10)

# Generate multiple IDs at once
ids = generate_batch(count=10, length=5)
for id in ids:
    print(id)
```

### Script Selection

```python
# Single script
devanagari_id = generate_id(scripts=['devanagari'])
tamil_id = generate_id(scripts=['tamil'])

# Multiple scripts
mixed_id = generate_id(scripts=['devanagari', 'tamil', 'gujarati'])

# Available scripts
from indic_uid import get_available_scripts
print(get_available_scripts())
# Output: ['devanagari', 'gujarati', 'kannada', 'tamil', 'telugu', 'bengali', 'english']
```

### Pronounceable IDs

Generate IDs that alternate between consonants and vowels for easier pronunciation:

```python
# Pronounceable ID (easier to speak)
id = generate_id(pronounceable=True, scripts=['devanagari'])
print(id)  # Example: 'कअखइगउ' (ka-khi-gu)

# Works with any script
id = generate_id(pronounceable=True, scripts=['tamil'])
print(id)  # Example: 'கஅசஇடஉ'
```

### Validation

```python
from indic_uid import is_valid_id, get_script_of_char

# Validate an ID
id = generate_id()
print(is_valid_id(id))  # True
print(is_valid_id('abc123'))  # False

# Validate with specific script
id = generate_id(scripts=['kannada'])
print(is_valid_id(id, scripts=['kannada']))  # True
print(is_valid_id(id, scripts=['tamil']))    # False

# Validate length
print(is_valid_id(id, length=6))  # True if ID is 6 chars

# Detect script of a character
char = 'क'
print(get_script_of_char(char))  # 'devanagari'
```

### Collision Probability Analysis

```python
from indic_uid import calculate_collision_probability, estimate_safe_id_count

# Calculate collision probability for your use case
prob = calculate_collision_probability(
    num_ids=10000,      # Expected number of IDs
    length=6,           # ID length
    num_scripts=6       # Number of scripts used
)
print(f"Collision probability: {prob:.2e}")
# Output: Collision probability: 5.45e-10 (extremely low!)

# Estimate safe number of IDs
safe_count = estimate_safe_id_count(
    length=6,
    num_scripts=6,
    max_collision_prob=0.000001  # 1 in a million
)
print(f"Safe ID count: {safe_count:,}")
# Output: Safe ID count: 13,856,406
```

## 🎯 Use Cases

### Referral System

```python
from indic_uid import generate_id

def create_referral_code(user_id):
    """Generate a unique referral code for a user."""
    referral_code = generate_id(length=6, scripts=['devanagari'])
    # Store mapping: referral_code -> user_id in database
    return referral_code

# Usage
code = create_referral_code(user_id=12345)
print(f"Your referral code: {code}")
# Share: https://yourapp.com/ref/{code}
```

### Short URLs

```python
from indic_uid import generate_id

def create_short_url(long_url):
    """Create a short URL identifier."""
    short_id = generate_id(length=5, scripts=['devanagari', 'gujarati'])
    # Store mapping: short_id -> long_url
    return f"https://short.link/{short_id}"

url = create_short_url("https://example.com/very/long/url/path")
print(url)  # https://short.link/कખગઘચ
```

### Coupon Codes

```python
from indic_uid import generate_id

def create_coupon_code(campaign_name):
    """Generate pronounceable coupon codes."""
    code = generate_id(
        length=6,
        pronounceable=True,
        scripts=['devanagari']
    )
    return code.upper()  # Note: Indian scripts don't have uppercase

coupon = create_coupon_code("diwali_sale")
print(f"Coupon: {coupon}")
```

## 📊 Collision Probability

With default settings (6 characters, all 7 scripts):

| Number of IDs | Collision Probability | Odds |
|--------------|----------------------|------|
| 1,000 | 5.45 × 10⁻¹² | 1 in 183 billion |
| 10,000 | 5.45 × 10⁻¹⁰ | 1 in 1.8 billion |
| 100,000 | 5.45 × 10⁻⁸ | 1 in 18 million |
| 1,000,000 | 5.45 × 10⁻⁶ | 1 in 183,000 |

**Conclusion**: Extremely safe for most applications. Even with 1 million IDs, collision probability is less than 0.0005%.

## 🌐 Supported Scripts

| Script | Example Characters | Total Characters |
|--------|-------------------|------------------|
| Devanagari (Hindi) | अ, क, ख, ग, घ | 41 |
| Gujarati | અ, ક, ખ, ગ, ઘ | 41 |
| Kannada | ಅ, ಕ, ಖ, ಗ, ಘ | 44 |
| Tamil | அ, க, ங, ச, ஞ | 30 |
| Telugu | అ, క, ఖ, గ, ఘ | 44 |
| Bengali | অ, ক, খ, গ, ঘ | 40 |
| English | a, b, c, d, e | 26

**Total character pool**: ~240 characters across all scripts

## 🔧 API Reference

### `generate_id(length=6, scripts=None, pronounceable=False)`

Generate a unique ID.

**Parameters:**
- `length` (int): Length of the ID (default: 6)
- `scripts` (list): List of script names to use (default: all scripts)
- `pronounceable` (bool): Alternate vowels/consonants (default: False)

**Returns:** String containing the generated ID

**Example:**
```python
id = generate_id(length=8, scripts=['devanagari', 'tamil'])
```

---

### `generate_batch(count, length=6, scripts=None, pronounceable=False)`

Generate multiple IDs at once.

**Parameters:**
- `count` (int): Number of IDs to generate
- `length` (int): Length of each ID
- `scripts` (list): List of script names
- `pronounceable` (bool): Alternate vowels/consonants

**Returns:** List of generated IDs

**Example:**
```python
ids = generate_batch(100, length=5)
```

---

### `is_valid_id(id_string, scripts=None, length=None)`

Validate if a string is a valid Indic ID.

**Parameters:**
- `id_string` (str): The ID to validate
- `scripts` (list): Expected scripts (default: any)
- `length` (int): Expected length (default: any)

**Returns:** Boolean

**Example:**
```python
is_valid = is_valid_id('कखگઘచঅ', scripts=['devanagari'])
```

---

### `get_script_of_char(char)`

Identify which script a character belongs to.

**Parameters:**
- `char` (str): A single character

**Returns:** Script name (str) or None

**Example:**
```python
script = get_script_of_char('क')  # Returns 'devanagari'
```

---

### `get_available_scripts()`

Get list of all available scripts.

**Returns:** List of script names

**Example:**
```python
scripts = get_available_scripts()
# ['devanagari', 'gujarati', 'kannada', 'tamil', 'telugu', 'bengali']
```

---

### `calculate_collision_probability(num_ids, length=6, num_scripts=6)`

Calculate collision probability for given parameters.

**Parameters:**
- `num_ids` (int): Expected number of IDs
- `length` (int): ID length
- `num_scripts` (int): Number of scripts being used

**Returns:** Float between 0 and 1

---

### `estimate_safe_id_count(length=6, num_scripts=6, max_collision_prob=0.000001)`

Estimate safe number of IDs for given collision probability.

**Parameters:**
- `length` (int): ID length
- `num_scripts` (int): Number of scripts
- `max_collision_prob` (float): Maximum acceptable collision probability

**Returns:** Integer (estimated safe count)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone the repo
git clone https://github.com/aayush-mor13/indic-uid.git
cd indic-uid

# Install in development mode
pip install -e .

# Install dev dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run tests with coverage
pytest --cov=indic_uid
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Aayush Mor** - [@aayush-mor13](https://github.com/aayush-mor13)
- **Jay Gala** - [@jaygala223](https://github.com/jaygala223)

## 🙏 Acknowledgments

- Inspired by the beauty and diversity of Indian scripts
- Built for the Indian developer community
- Thanks to all contributors!

## 📫 Support

- 🐛 [Report a bug](https://github.com/aayush-mor13/indic-uid/issues)
- 💡 [Request a feature](https://github.com/aayush-mor13/indic-uid/issues)
- ⭐ Star this repo if you find it useful!

## 📈 Changelog

### v0.1.0 (2025-01-22)
- Initial release
- Support for 6 Indian scripts + English
- Random and pronounceable ID generation
- Validation and script detection
- Collision probability analysis

---

Made with ❤️ for the Indian developer community
