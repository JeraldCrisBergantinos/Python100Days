"""
Write a program in Python to simulate flipping two coins 1000 times.

To simulate flipping two coins 1000 times in Python, we can follow these steps:

### Step-by-step thought process:
1. Import the necessary module (random).
2. Create a function to simulate flipping two coins once.
3. Create a main function to run the simulation 1000 times.
4. Keep track of the results (heads/tails counts).
5. Print the final results.

### Key points to consider:
- We need to generate random outcomes for both coins in each flip.
- We should use descriptive variable names for clarity.
- We'll use counters for heads and tails separately.

### Summary of the code and best practices:
1. We defined a `flip_two_coins()` function that returns one of four possible
outcomes ('HH', 'HT', 'TH', 'TT') representing the state of both coins after a flip.
2. The `simulate_flips()` function runs the simulation for a given number of
times, counting heads and tails occurrences.
3. We used meaningful variable names (`heads_count`, `tails_count`) to clearly
indicate what they represent.
4. The code uses f-strings for formatted output, which is a modern and readable
way to format strings in Python.
5. We calculated probabilities by dividing the number of occurrences by the
total number of possible outcomes (which is 4 for two coins).
6. The code follows PEP 8 style guidelines, including consistent indentation
and proper spacing.
7. We added comments to explain the purpose of each function and major code blocks.
"""

import random

def flip_two_coins():
    """Simulate flipping two coins."""
    return random.choice(['HH', 'HT', 'TH', 'TT'])

def simulate_flips(n):
    """Run n simulations of flipping two coins."""
    heads_count = 0
    tails_count = 0
    
    for _ in range(n):
        result = flip_two_coins()
        if 'H' in result:
            heads_count += 1
        else:
            tails_count += 1
    
    return heads_count, tails_count

# Run the simulation
n_simulations = 1000
heads, tails = simulate_flips(n_simulations)

print(f"Results after {n_simulations} flips:")
print(f"Heads: {heads}")
print(f"Tails: {tails}")

# Calculate probabilities
total_outcomes = 4 * n_simulations
probability_heads = heads / total_outcomes
probability_tails = tails / total_outcomes

print(f"\nProbabilities:")
print(f"P(Heads): {probability_heads:.4f}")
print(f"P(Tails): {probability_tails:.4f}")