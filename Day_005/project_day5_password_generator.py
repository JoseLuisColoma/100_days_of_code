import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")
nr_letters = int(input("How many letters would you like in your password?:\n"))
nr_numbers = int(input("How many numbers would you like in your password?:\n"))
nr_symbols = int(input("How many symbols would you like in your password?:\n"))

# EASY LEVEL: password with concatenated letters, symbols and numbers
# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#
# for number in range(1, nr_symbols + 1):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
#
# for number in range(1, nr_numbers + 1):
#     random_number = random.choice(numbers)
#     password += random_number
#
# print(password)

# HARD LEVEL: password using letters, symbols and numbers in random position
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"password: {password}")
