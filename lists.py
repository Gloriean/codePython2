mylist = ["apple", "orange", "banana"]
mylist.insert(1, "pawpaw")
print(mylist)
mylist.append("grape")
print(mylist)

mylist = ["apple", "orange", "banana"]
trophical = ("rain forest", "sahara desert", "swappy area")
var = (1, 2, 3)
mylist.extend(trophical)
mylist.extend(var)
print(mylist)
print(type(mylist))
print(mylist[0])
print(len(mylist))



if "grape" in mylist:
    print("YES!")
else:
    print("NO!")


#looping through a list
#for loop
thislist = ["ratio", "proportion", "percentage"]
for x in range(len(thislist)):
    print(x)


#while loop
thislist1 = ["break", "breakable", "unbreak", "unbreakable"]
i = 0
while i < len(thislist1):
    print(thislist1[i])
    i = i + 1


#sorting list
cln = ["washing machine", "cooking utensils", "bathroom tools"]
cln.sort()
print(cln)