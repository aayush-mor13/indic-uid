import math


def calculate_collision_probability(num_ids, length=6, num_scripts=6):
    """
    Calculate the probability of collision for given parameters.
    Uses the birthday problem formula.
    
    Args:
        num_ids: Number of IDs to generate
        length: Length of each ID
        num_scripts: Number of scripts being used
    
    Returns:
        float: Collision probability (0 to 1)
    """
    # Approximate average characters per script
    avg_chars_per_script = 40
    total_chars = avg_chars_per_script * num_scripts
    
    # Total possible IDs
    total_combinations = total_chars ** length
    
    # Birthday problem: P(collision) ≈ 1 - e^(-n²/2N)
    # where n = number of IDs, N = total combinations
    
    exponent = -(num_ids ** 2) / (2 * total_combinations)
    probability = 1 - math.exp(exponent)
    
    return probability


def estimate_safe_id_count(length=6, num_scripts=6, max_collision_prob=0.000001):
    """
    Estimate how many IDs can be safely generated with given collision probability.
    
    Args:
        length: Length of each ID
        num_scripts: Number of scripts being used
        max_collision_prob: Maximum acceptable collision probability (default: 1 in 1 million)
    
    Returns:
        int: Estimated safe number of IDs
    """
    avg_chars_per_script = 40
    total_chars = avg_chars_per_script * num_scripts
    total_combinations = total_chars ** length
    
    # Rearranging birthday problem: n ≈ sqrt(-2N * ln(1-p))
    safe_count = math.sqrt(-2 * total_combinations * math.log(1 - max_collision_prob))
    
    return int(safe_count)
