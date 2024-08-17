#listing a function
def  myFunction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

myFunction(fruits)

#Lambda function
a = lambda x: x + 10
print(a(5))

b = lambda y, z: y * z
print(b(5, 6))

c = lambda d, e, f: d + e + f
print(c(5, 6, 7))


#Default parameter value
def func(country = "Nigeria"):
    print("I am from " + country)


func("Mexico")
func("Italy")
func()
func("Brazil")

#using the return statement
def fun1(y):
    return 5 * y

print(fun1(9))
print(fun1(72))