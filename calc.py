import math as mt

print(mt.sqrt(25))

print(mt.pi)

from datetime import datetime

today = datetime.today()

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

print("\nHour:", Time.hour)
print("Minute:", Time.minute)
print("Seconds:", Time.second)


from datetime import datetime

a = datetime(1999, 12, 12, 12, 12, 12, 12)
print("\nYear =", a.year)
print("Month =", a.month)
print("Day =", a.day)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Seconds =", a.second)
print("Timestamp =", a.timestamp())