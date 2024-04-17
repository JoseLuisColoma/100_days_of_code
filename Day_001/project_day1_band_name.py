# Strategy
# 1.- Create a greeting for your program
# 2.- Ask the user for the city that they grew up in
# 3.- Ask the user for the name of a pet
# 4.- Combine the name o hteir city and pet and them their band name
# 5.- Make sure the input cursor shows on a new line.

print("Welcome to The Band Name Generator!")
city = input("What city did you grow up in?:\n").upper()
pet = input("What is the name of your first pet?\n").upper()
print(f"Your band name could be \'{city} {pet}\'")