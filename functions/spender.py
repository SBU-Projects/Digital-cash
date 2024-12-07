class Spender:

    def __init__(self, name, public_data):
        print("The {} bank constructor is called!".format(name))
        self.public_data = public_data
        self.name = name
        self.x = 0
        for n in name:
            self.u += ord(n)