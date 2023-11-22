#If... else statement 
#Use if statements when you want to execute a block of code only if a certain condition is true.

a = 60
b = 33

if (b > a):
    print("b is greater than a")
elif (a == b):
    print("they are both equal")
else:
    print("no condition is met\n")



#While loop statement
#Use while loops when you want to repeatedly
#execute a block of code as long as a certain condition is true.
#first while statement
i = 1
while (i < 6):
    print(i)
    if (i == 3):
        break
    i += 1



#second while statement
c = 0;
while (c < 5):
    c += 1;
    if (c == 3):
        continue
    print(c)





#For loop statement
#Use for loops when you want to iterate over a
#sequence (such as a list, tuple, or string) or any iterable object.
#first for loop

order = ("lists", "sets", "tuples", "dicts")

for y in order:
    print(y)
    if y == 'tuples':
        break


#second for loop
for letter in "Learning to Code":
    if letter == 'e' or letter == 'g':
        continue
    print('Current Letter: \n', letter)
else:
        print("Finally Finished!\n")




#third for loop
#nested loop

fruits = ["oranges", "mangoes", "bananas"]
colours = ["red", "yellow", "green"]

for m in fruits:
    for n in colours:
        print(m, n)