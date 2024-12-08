import random
class Bank:
    def __init__(self, name, public_data):
        print("The {} bank constructor is called!".format(name))
        self.public_data = public_data
        self.name = name
        self.x = 0
        for n in name:
            self.x += ord(n)

        p = self.public_data["p"]
        g = self.public_data["g"]
        self.h = pow(g, self.x, p)

        self.conected_spenders = []

    def get_public_arguments_by_index(self, index):
        public_arguments = self.get_public_arguments()
        data = public_arguments[index]
        return data


    def get_public_idetifiers(self):
        data = {
            "id": self.h,
            "name": self.name
        }

        return data

    def connect_with_spender(self, spender_data):
        connection = {
            "account number": spender_data["account number"],
            "name": spender_data["name"]
        }
        self.conected_spenders.append(connection)
        public_data = self.public_data
        g2 = public_data['g2']
        p = public_data['p']
        z_prime = pow((connection["account number"]*g2), self.x, p)

        return z_prime

    def get_conected_spenders(self):
        return self.conected_spenders


    def creating_coin_bank(self, order, input_tuple):
        if order == "gw":
            w = random.randint(1000, 2000)
            g = self.get_public_arguments_by_index("g")
            p = self.get_public_arguments_by_index("p")
            gw = pow(g, w, p)

            return gw
