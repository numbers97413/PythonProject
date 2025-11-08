import random

def generate_norwegian_lotto_numbers():
    lotto_numbers = random.sample(range(1, 35), 7)
    lotto_numbers.sort()
    return lotto_numbers

numbers = []
for i in range(10):
    numbers.append(generate_norwegian_lotto_numbers())
print("Dine Lotto tall er:")
print(numbers)