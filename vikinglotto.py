import random

def generate_vikinglotto_numbers():
    # Generate 6 unique main numbers from 1 to 48
    main_numbers = random.sample(range(1, 49), 6)
    main_numbers.sort()  # Sort for readability
    # Generate 1 Viking number from 1 to 5
    viking_number = random.randint(1, 5)
    return main_numbers, viking_number

# Generate and print the numbers
main_nums, viking_num = generate_vikinglotto_numbers()
print(f"Main Numbers: {main_nums}")
print(f"Viking Number: {viking_num}")