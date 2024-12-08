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
        public_arguments = self.get_public_arguments()
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


