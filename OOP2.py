#Polymorphism
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")       #Create a Car class
boat = Boat("Ibiza", "Touring 20") #Create a Boat class
plane = Plane("Boeing", "747")     #Create a Plane class

for x in (car, boat, plane):
  x.move()



#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")
    
class Car(Vehicle):
   pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Toyota", "Corolla")
boat1 = Boat("Lirine", "Touring 27")
plane1 = Plane("Arik", "787")


for y in (car1, boat1, plane1):
   print(y.brand)
   print(y.model)
   y.move()