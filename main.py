



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
