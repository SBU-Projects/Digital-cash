class Bank:
    def __init__(self, name, public_data):
        print("The {} bank constructor is called!".format(name))
        self.public_data = public_data
        self.x = 0
        for n in name:
            self.x += ord(n)

    def compute_public_identifier(self):
        p = self.public_data["p"]
        g = self.public_data["g"]
        h = pow(g, self.x, p)

        return h