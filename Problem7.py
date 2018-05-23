# What is the 10001st prime number?

# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
def isPrime(n):
    # line 6, checks for 0 and 1, which are not prime numbers
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns the nth prime number
def nthPrime(n):
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

print(nthPrime(10001))

# Answer: 104743
