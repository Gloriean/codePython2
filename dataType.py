x = 5;
print(type(x));

t = 56.0;
print(type(t));

a = 1j;
print(type(a));

y = 'hi!';
print(type(y));

m = list(("orange", "banana", "mango"));
print(type(m));

n = tuple(("orange", "carrot", "apple"));
print(type(n));

o = True;
print(type(o));

r = range(6);
print(type(r));

z = ["name", "Esther"];
print(type(z));

s = set(("colour", "range"));
print(type(s));


#Converting from one datatype to another.
B = 2;
C = 56.7;
D = 5j;

#convert from int to float
b = float(B);
print(b);

#convert from float to int
c = int(C);
print(c);

#convert from int to complex
d = complex(B);
print(d);

print(type(b));
print(type(c));
print(type(d));