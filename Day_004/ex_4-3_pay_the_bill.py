import random

names = ["Angela", "Ben", "Jenny", "Michael", "Cloe"]

num_items = len(names)

random_choice = random.randint(0, num_items-1)
person_will_pay = names[random_choice]
print(f'{person_will_pay} is going to pay the mail today!')