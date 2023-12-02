import math as mt

print(mt.sqrt(25))

print(mt.pi)

from datetime import date

today = date.today()

print("Current Year is:", today.year)
print("Current Month is:", today.month)
print("Current Day is:", today.day)

from datetime import time

my_time = time(13, 24, 56)
print("\nEntered Time:", my_time)

my_time = time(minute=12)
print("\nTime with one argument", my_time)

my_time = time()
print("\nTime without argument", my_time)


from datetime import time

Time = time(12, 22, 45)

print("Hour:", Time.hour)
print("Minute:", Time.minute)
print("Seconds:", Time.second)