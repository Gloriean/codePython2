a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print(len(a))

txt = "all is well"
print("well" not in txt)
print("all" in txt)

if "alloo" not in txt:
    print("True")
else:
    print(False)


#change to uppercase
x = "cool"
print(x.upper())

#change to lowercase
y = "COoL"
print(y.lower())

#remove whitespace
z = " It's been rainy all day "
print(z.strip())

#replace
b = "longitude, latitude!"
print(b.replace("l", "h"))
print(b.encode())


#string concatenation
txt1 = "Hello,"
txt2 = "Felix!"
print(txt1 + " " + txt2)

#format string
age = 56
txt3 = "My name is John, and I'm {} years old."
print(txt3.format(age))


qty = 3
itemno = 45
price = 78.90
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(qty, itemno, price))

myride = "I have a {carname}, it is a {model}"
print(myride.format(carname = "Ford", model = "Mustang"))
