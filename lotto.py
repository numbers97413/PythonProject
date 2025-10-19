import random

def generate_norwegian_lotto_numbers():
    # Generate 7 unique random numbers between 1 and 34
    lotto_numbers = random.sample(range(1, 35), 7)
    # Sort the numbers for better readability
    lotto_numbers.sort()
    return lotto_numbers

# Generate and print the numbers
numbers = generate_norwegian_lotto_numbers()
print("Dine Norske Lotto tall er:")
print(numbers)