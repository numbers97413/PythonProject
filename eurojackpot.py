import random

def generate_eurojackpot_numbers():
    """
    Generate random EuroJackpot numbers:
    - 5 unique main numbers from 1 to 50
    - 2 unique Euro numbers from 1 to 12
    """
    main_numbers = sorted(random.sample(range(1, 51), 5))
    euro_numbers = sorted(random.sample(range(1, 13), 2))
    return main_numbers, euro_numbers

# Generate and print the numbers
main, euro = generate_eurojackpot_numbers()
print("Main numbers:", ", ".join(map(str, main)))
print("Euro numbers:", ", ".join(map(str, euro)))