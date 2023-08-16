from Animal import Animal
class Dog(Animal):
    def __init__(self, name, breed, is_active, color, weight, sex, obedience):
        self.name = name
        self.breed = breed
        self.is_active = is_active
        self.color = color
        self.weight = str(weight) + "lbs"
        self.sex = sex
        self.obedience = obedience

    def was_good_doggo(self):
        if self.obedience == "The Goodest":
            return print(self.name + " is the goodest doggo!")
        else:
            return

