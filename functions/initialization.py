from sympy import isprime, nextprime, primitive_root
import random

class Initialization:
    def __init__(self, large_prime_number):
        print("Initializing with large prime {}".format(large_prime_number))
        self.p = large_prime_number
        self.set_public_arguments()

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

    def private_key_generator(self):
        k1 = random.randint(0, 4096)
        for k2 in range(self.q, self.q + (2*self.q)):
            if (k1 % self.q) == (k2 % self.q):
                return (k1, k2)

    def set_public_arguments(self):
        print("set_public_arguments functio is called!")
        self.q = self.generate_prime_pair()
        self.g = self.find_square_of_primitive_root()


    def get_public_arguments(self):
        keys = self.private_key_generator()
        data = {
            "p": self.p,
            "q": self.q,
            "g": self.g,
            "g1": pow(self.g, keys[0], self.p),
            "g2": pow(self.g, keys[1], self.p)
        }
        return data

    def get_private_arguments(self):
        keys = self.private_key_generator()
        data = {
            "k1": keys[0],
            "k2": keys[1]
        }

        return data
