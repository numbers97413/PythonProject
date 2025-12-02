a = 0
b = 1
n = 0
fibonacci_tal = [0, 1]
while n < 50:
    c = a + b

    fibonacci_tal.append(c)
    a = b
    b = c
    n = n + 1
print(fibonacci_tal)