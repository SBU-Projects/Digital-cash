from sympy import isprime, nextprime, primitive_root

def generate_prime_pair():
    p = 28871271685163  # Start with the smallest prime number
    while True:
        p = nextprime(p)  # Find the next prime number
        q = (p - 1) // 2  # Calculate q
        if isprime(q):  # Check if q is also prime
            return p, q



def find_square_of_primitive_root(p):
    # Find a primitive root modulo p
    g0 = primitive_root(p)
    # Calculate the square of the primitive root modulo p
    g = pow(g0, 2, p)
    return g0, g



# Generate the prime pair
prime_p, prime_q = generate_prime_pair()
# Find the square of a primitive root modulo the prime p
primitive_root_g0, square_g = find_square_of_primitive_root(prime_p)
print(prime_p, prime_q)
print(primitive_root_g0, square_g)
