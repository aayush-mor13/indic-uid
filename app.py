import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PARENT_DIR)

from indic_ids.generator import generate_id, generate_batch
from indic_ids.validators import is_valid_id, get_script_of_char
from indic_ids.character_sets import get_available_scripts
from indic_ids.utils import calculate_collision_probability, estimate_safe_id_count

def main():
    print("=== Indic IDs Library Demo ===\n")

    # 1. Basic generation
    print("1. Basic ID generation (all scripts):")
    for _ in range(5):
        print(f"   {generate_id()}")

    # 2. Script-specific generation
    print("\n2. Devanagari-only IDs:")
    for _ in range(5):
        print(f"   {generate_id(scripts=['devanagari'])}")

    # 3. Pronounceable IDs
    print("\n3. Pronounceable IDs (Devanagari):")
    for _ in range(5):
        print(f"   {generate_id(scripts=['devanagari'], pronounceable=True)}")

    # 4. Mixed scripts
    print("\n4. Mixed scripts (Devanagari + Gujarati):")
    for _ in range(5):
        print(f"   {generate_id(scripts=['devanagari', 'gujarati'])}")

    # 5. English-only generation
    print("\n English-only IDs:")
    for _ in range(5):
        print(f"   {generate_id(scripts=['english'])}")

    # 6. Pronounceable English IDs
    print("\n Pronounceable English IDs:")
    for _ in range(5):
        print(f"   {generate_id(scripts=['english'], pronounceable=True)}")

    # 7. Short English IDs
    print("\n Short English IDs (length=4):")
    for _ in range(5):
        print(f"   {generate_id(scripts=['english'], length=4)}")

    # 8. Batch generation
    print("\n5. Batch generation (10 IDs):")
    batch = generate_batch(10, length=5)
    for id_ in batch:
        print(f"   {id_}")

    # 9. Validation
    print("\n6. Validation:")
    test_id = generate_id(scripts=['kannada'])
    print(f"   Generated: {test_id}")
    print(f"   Is valid: {is_valid_id(test_id)}")
    print(f"   Is valid Kannada: {is_valid_id(test_id, scripts=['kannada'])}")
    print(f"   Is valid Tamil: {is_valid_id(test_id, scripts=['tamil'])}")

    # 10. Script detection
    print("\n7. Script detection:")
    test_chars = [generate_id(length=1, scripts=[s]) for s in ['devanagari', 'tamil', 'bengali']]
    for char in test_chars:
        print(f"   '{char}' is from: {get_script_of_char(char)}")

    # 11. Collision probability
    print("\n8. Collision probability analysis:")
    print(f"   Available scripts: {get_available_scripts()}")
    prob = calculate_collision_probability(num_ids=10_000, length=6, num_scripts=6)
    print(f"   Collision probability for 10K IDs (6 chars, 6 scripts): {prob:.10f}")
    print(f"   That's 1 in {int(1/prob) if prob > 0 else 'infinity'}")

    safe_count = estimate_safe_id_count(length=6, num_scripts=6)
    print(f"   Safe ID count (collision prob < 0.0001%): {safe_count:,}")




if __name__ == "__main__":
    main()