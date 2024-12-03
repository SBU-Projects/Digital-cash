class Bank:
    def __init__(self, name, public_data):
        print("The {} bank constructor is called!".format(name))
        self.public_data = public_data
        self.x = 0
        for n in name:
            self.x += ord(n)

        print(self.x)