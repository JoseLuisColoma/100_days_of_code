import random as rd
import my_module

random_integer = rd.randint(1,10)
print(random_integer)
print(my_module.PI)

# 0.000 - 0.999
random_float = round(rd.random(),3)
print(random_float)

# 0.000 - 4.999
random_float = round(rd.random()*5, 3)
print(random_float)

love_score = rd.randint(1,100)
print(f"Your love score is {love_score}")