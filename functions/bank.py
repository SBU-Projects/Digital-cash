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



        return h

    def get_public_idetifiers(self):
        data = {
            "id": self.compute_public_identifier(),
            "name": self.name
        }

        return data