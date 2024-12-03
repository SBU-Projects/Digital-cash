from sympy import isprime, nextprime, primitive_root

class Initialization:
    def __init__(self, large_prime_number):
        print("Initializing with large prime {}".format(large_prime_number))
        self.p = large_prime_number

    def generate_prime_pair(self):
        curr_p = self.p
        while True:
            curr_p = nextprime(curr_p)  # Find the next prime number
            q = (curr_p - 1) // 2  # Calculate q
            if isprime(curr_p):  # Check if q is also prime
                return q

    def find_square_of_primitive_root(self):
        g0 = primitive_root(self.p)
        # Calculate the square of the primitive root modulo p
        g = pow(g0, 2, self.p)
        return g

    def set_public_arguments(self):
        self.q = self.generate_prime_pair()
        self.g = self.find_square_of_primitive_root()

