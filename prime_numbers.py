def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    # Check for divisibility from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print prime numbers from 1 to 100
print("Prime numbers between 1 and 100 are:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")