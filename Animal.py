class Animal:

    def __init__ (self, name):
        self.name = name
    def is_mammal(self):
        print(str(self.name) + " is a mammal")

    def is_quadriped(self):
        print(str(self.name) + " is a quadriped")