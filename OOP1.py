class HND:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello, my name is " + self.name + " and I work for a Canadian " + self.company +  ".")

p = HND("Glory", "Company")
p.show()


#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

d = Person("Ope", "Ayorinde")
d.printname()
