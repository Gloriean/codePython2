class HND:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello, my name is " + self.name + " and I work for a Canadian " + self.company +  ".")

p = HND("Glory", "Company")
p.show()


#Inheritance
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

d = Person("Ope", "Ayorinde")
d.printname()


#Iteration
fruits = ["apple", "banana", "carrot"]

myit = iter(fruits)
print(next(myit))
print(next(myit))
print(next(myit))


#Iterating a String
str = 'Iterating'

myit = iter(str)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Looping through an iteration

colour = ["red", "blue", "yellow", "purple"]

for x in colour:
    print(x)


#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))