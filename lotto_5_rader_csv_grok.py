import random
from datetime import date
import csv

def generate_norwegian_lotto_numbers():
    lotto_numbers = random.sample(range(1, 35), 7)
    lotto_numbers.sort()
    return lotto_numbers

# Generate 10 sets of lotto numbers
numbers = []
for i in range(10):
    numbers.append(generate_norwegian_lotto_numbers())

# Get today's date
today = date.today().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD

# Prepare data for CSV: [date, num1, num2, num3, num4, num5, num6, num7]
csv_data = []
for row in numbers:
    csv_data.append([today] + row)

# Write to CSV file
with open('lotto_numbers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Date', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7'])
    # Write all rows
    writer.writerows(csv_data)

# Print confirmation and sample
print("Dine Lotto tall er:")
for i, row in enumerate(numbers, 1):
    print(f"Rad {i}: {row}")

print(f"\nData lagret til 'lotto_numbers.csv' med dato: {today}")