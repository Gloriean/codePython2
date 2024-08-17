thisdict = {
    "name": "Sarah",
    "age": 22,
    "hobby": "singing"
}

print(thisdict)
print(thisdict["age"])
print(len(thisdict))
print(type(thisdict))

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

#looping through a dict
if "name" in thisdict:
    print("Yes, it's present in the dict keys")

for x, y in thisdict.items():
    print(x, y)
    

#Nested Dictionaries
family = {
    "fam1": {
        "surname": "Olajide",
        "children": 4,
        "religion": "christianity"
    },

    "fam2": {
        "surname": "Ayinde",
        "children": 2,
        "religion": "islam"
    },
    "fam3": {
        "surname": "Okoye",
        "children": 3,
        "religion": "muslim"
    }
}
print(family)