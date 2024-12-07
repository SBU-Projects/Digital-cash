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



    def get_public_idetifiers(self):
        data = {
            "account number": self.I,
            "name": self.name
        }

        return data

    def connect_with_bank(self, bank):
        self.z_prime = bank.connect_with_spender(self.I)
        print(self.z_prime)

