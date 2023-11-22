#set in python
myset = {"apple", "banana", "pawpaw"}
myset.add("grape")
print(myset)
print(len(myset))
print(type(myset))

myset1 = {"bag", "clothes", "cream"}
myset3 = {"gauge", "spin"}
myset1.update(myset3)
print(myset1)
print("change" in myset1)

#looping in set
for x in myset:
    print(x)

