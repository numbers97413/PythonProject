text = input("Enter numbers separated by spaces: ")
number_strings = text.split()
numbers = []
for s in number_strings:
    numbers.append(int(s))
counts = {}
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1
print(counts, numbers)
duplicates = []
for num in counts:
    if counts[num] > 1:
        duplicates.append(num)
if not duplicates:
    result = "No duplicates\nList: " + str(numbers)
else:
    result = "Duplicates: " + str(duplicates) + "\nList: " + str(numbers)
print(result)