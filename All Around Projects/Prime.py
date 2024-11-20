def is_prime(n):
    """Check if a number is prime."""
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n == 2 or n == 3:
        return True
    # Eliminate even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for factors from 5 upwards, skipping even numbers and multiples of 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def first_n_primes(n):
    """Find the first n prime numbers."""
    primes = []  # List to store prime numbers
    count = 0    # Counter for the number of primes found
    number = 2   # Starting number to check for primality
    while count < n:
        if is_prime(number):
            primes.append(number)  # Add prime number to the list
            count += 1             # Increment prime count
        number += 1  # Check the next number
    return primes

# Find the first 100 prime numbers
prime_numbers = first_n_primes(100)

# Calculate the sum of the prime numbers
sum_of_primes = sum(prime_numbers)

# Calculate the product of the prime numbers
product_of_primes = 1
for prime in prime_numbers:
    product_of_primes *= prime

# Print the results
print("Sum of the first 100 prime numbers:", sum_of_primes)
print("Product of the first 100 prime numbers:", product_of_primes)
