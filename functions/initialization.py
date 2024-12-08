from sympy import isprime, nextprime, primitive_root
import random
from cryptography.hazmat.primitives.hashes import Hash, SHA256
from cryptography.hazmat.backends import default_backend


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

    def get_public_arguments_by_index(self, index):
        public_arguments = self.get_public_arguments()
        data = public_arguments[index]
        return data

    def get_private_arguments(self):
        keys = self.private_key_generator()
        data = {
            "k1": keys[0],
            "k2": keys[1]
        }

        return data

    def hash_H(self, input_tuple):
        q = self.get_public_arguments_by_index("q")
        if len(input_tuple) != 5:
            raise ValueError("Input must be a 5-tuple of integers.")
        input_bytes = ','.join(map(str, input_tuple)).encode('utf-8')
        digest = Hash(SHA256(), backend=default_backend())
        digest.update(input_bytes)
        hash_digest = digest.finalize()

        return int.from_bytes(hash_digest, 'big') % q

    def hash_H0(self, input_tuple):
        q = self.get_public_arguments_by_index("q")
        if len(input_tuple) != 4:
            raise ValueError("Input must be a 4-tuple of integers.")
        input_bytes = ','.join(map(str, input_tuple)).encode('utf-8')
        digest = Hash(SHA256(), backend=default_backend())
        digest.update(input_bytes)
        hash_digest = digest.finalize()
        return int.from_bytes(hash_digest, 'big') % q

    def creating_coin(self, bank, spender):

        gwBetha = bank.creating_coin_bank("gw-betha", {"spender account number": spender.get_public_arguments_by_index("account number")})
        ABzab = spender.creating_coin_spender("ABzab", gwBetha)

        return ABzab
