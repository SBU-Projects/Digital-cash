import random
class Spender:

    def __init__(self, name, public_data):
        print("{} constructor is called as a spender!".format(name))
        self.public_data = public_data
        self.name = name
        self.u = 0
        for n in name:
            self.u += ord(n)

        g1 = public_data['g1']
        p = public_data['p']
        self.I = pow(g1, self.u, p)

    def get_public_arguments_by_index(self, index):
        public_arguments = self.public_data
        data = public_arguments[index]
        return data

    def get_public_idetifiers(self):
        data = {
            "account number": self.I,
            "name": self.name
        }

        return data

    def connect_with_bank(self, bank):
        print("{} conected to {} bank".format(self.name, bank.get_public_idetifiers()['name']))
        self.z_prime = bank.connect_with_spender(self.get_public_idetifiers())


    def creating_coin_spender(self, order, input_tuple):
        if self.z_prime > 0:
            if order == "ABzab":
                random_variables = {
                    "s": random.randint(1000, 2000),
                    "x1": random.randint(1000, 2000),
                    "x2":  random.randint(1000, 2000),
                    "alpha1": random.randint(1000, 2000),
                    "alpha2": random.randint(1000, 2000)
                }

                g = self.get_public_arguments_by_index("g")
                g1 = self.get_public_arguments_by_index("g1")
                g2 = self.get_public_arguments_by_index("g2")
                p = self.get_public_arguments_by_index("p")
                A = pow((self.I*g2), random_variables['s'], p)
                data = {
                    "A": A,
                    "B": (pow(g1, random_variables['x1']) * pow(g2, random_variables['x2']))%p,
                    "z": pow(self.z_prime, random_variables['s'], p),
                    "a": (pow(input_tuple["gw"], random_variables['alpha1'])*pow(g, random_variables['alpha2']))%p,
                    "b": (pow(input_tuple["betha"], random_variables['s']*random_variables['alpha1']) * pow(A, random_variables['alpha2'])) % p
                }

                return data
        else:
            raise ValueError("The sender does not connected to the bank!")


