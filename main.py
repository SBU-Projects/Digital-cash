from sympy import isprime, nextprime

def generate_prime_pair():
    p = 28871271685163  # Start with the smallest prime number
    while True:
        p = nextprime(p)  # Find the next prime number
        q = (p - 1) // 2  # Calculate q
        if isprime(q):  # Check if q is also prime
            return p, q

# Generate the prime pair
prime_p, prime_q = generate_prime_pair()
print(prime_p, prime_q)
