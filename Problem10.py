# Find the sum of all the primes below two million

def sum_primes(limit):
    primes = []
    for n in range(2, limit+1):
        # try dividing n with all primes less than sqrt(n):
        for p in primes:
            # if p divides n, stop the search
            if n % p == 0: break
            if n < p*p:
                # if p > sqrt(n), mark n as prime and stop search
                primes.append(n)
                break
        # fallback: we actually only get here for n == 2
        else: primes.append(n)
    return sum(primes)
    
print(sum_primes(2000000))

# Answer: 142913828922
