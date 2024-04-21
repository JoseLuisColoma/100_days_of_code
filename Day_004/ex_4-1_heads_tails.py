import random as rd

print("Heads and Tails")
number = rd.randint(0, 1)

if number == 0:
    print("Heads")
else:
    print("Tails")

print(number)