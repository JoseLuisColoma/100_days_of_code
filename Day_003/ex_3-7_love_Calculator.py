print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()
score = 0
combined_name = (name1 + name2).upper()
t = combined_name.count('T')
r = combined_name.count('R')
u = combined_name.count('U')
e = combined_name.count('E')
first_digit = t + r + u + e
l = combined_name.count('L')
o = combined_name.count('O')
v = combined_name.count('V')
e = combined_name.count('E')
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")