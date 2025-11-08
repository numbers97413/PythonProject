import random
from datetime import date
import csv
import os


def generate_norwegian_lotto_numbers():
    lotto_numbers = random.sample(range(1, 35), 7)
    lotto_numbers.sort()
    return lotto_numbers


# Generate 10 new sets of lotto numbers
numbers = []
for i in range(10):
    numbers.append(generate_norwegian_lotto_numbers())

# Get today's date
today = date.today().strftime("%Y-%m-%d")

# Prepare data: [date, num1, ..., num7]
csv_data = [[today] + row for row in numbers]

# Define CSV file
filename = 'lotto_numbers.csv'

# Check if file exists to decide whether to write header
file_exists = os.path.isfile(filename)

# Open in append mode ('a'), write header only if file is new
with open(filename, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write header only if file didn't exist before
    if not file_exists:
        writer.writerow(['Date', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7'])

    # Append the new rows
    writer.writerows(csv_data)

# Print the newly generated numbers
print("Dine nye Lotto-tall er lagt til i 'lotto_numbers.csv':")
for i, row in enumerate(numbers, 1):
    print(f"Rad {i}: {row}")

print(f"\nDato: {today} | 10 nye rader lagt til!")