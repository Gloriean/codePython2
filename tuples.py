#Packing a tuple
mytuple = ("ring", 1, 2, 3, True)
print(mytuple)

if "ringer" in mytuple:
    print("YES!")
else:
    print("NO!")

#Unpacking a tuple
thistuple = ("later", "now", "before")
(other, earlier, right) = thistuple
(work, it, out) = thistuple

print(other)
print(earlier)
print(right)

print(work)
print(it)
print(out)

#joining tuples
tup1 = ["biscuit", "cookies"]
tup2 = ["milk", "water"]
tup3 = tup1 + tup2
print(tup3)