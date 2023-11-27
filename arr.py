import array as arr

a = arr.array('i', [1, 2, 3])
a.append(10)
print(a)

b = arr.array('u', 'A')
print(b)

c = arr.array('d', [2.1, 3.4, 6.5])
d = arr.array('d', [44.5, 68.9, 1.0, 4.5])
c.extend(d)

for x in range(len(c)):
    print(x)

