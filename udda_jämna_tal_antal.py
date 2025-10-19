jämn = 0
udda = 0
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        jämn = jämn + 1
    else:
        udda = udda + 1
print(jämn, udda)
