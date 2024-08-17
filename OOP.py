class Dog:

    animal = 'Dog'

    def __init__(self, breed, colour, attr):
        self.breed = breed
        self.colour = colour
        self.attr = attr
    
Rodger = Dog("Pug", "White", "Hairy")
Kollen = Dog("Bulldog", "Brown", "Big")


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

#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(f"I am {self.firstname} {self.lastname}")

p1 = Person("Glory", "Olasanmi")
p1.printname()

