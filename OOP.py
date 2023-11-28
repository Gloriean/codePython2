class Dog:

    animal = 'Dog'

    def __init__(self, breed, colour, attr):
        self.breed = breed
        self.colour = colour
        self.attr = attr
    
Rodger = Dog("Pug", "White", "hairy")
Kollen = Dog("Bulldog", "Brown", "big")


print("Rodger Details:")
print("Rodger is a", Rodger.animal)
print("Rodger is a", Rodger.breed)
print("Its colour is", Rodger.colour)
print("It's", Rodger.attr)

print("\nKollen Details:")
print("Kollen is a", Kollen.animal)
print("Kollen is a", Kollen.breed)
print("Its colour is", Kollen.colour)
print("It's", Kollen.attr)

