MINIMUM_HEIGHT = 120
SUB12 = 12
SUB18 = 18
TICKET_SUB12 = 5
TICKET_SUB18 = 7
TICKET_ADULT = 12
PHOTO = 3
with_photo = False
print("Welcome to the roallercoaster!")
height = int(input("Type your height in cm: "))

price = 0
if height > MINIMUM_HEIGHT:
    print("You can ride the rollercoaster")
    age = int(input("Type your age: "))
    if age < SUB12:
        price = TICKET_SUB12
    elif age < SUB18:
        price = TICKET_SUB18
    else:
        price = TICKET_ADULT
    with_photo = input("Do you want a photo? (Y/N): ").upper()
    if with_photo == 'Y':
        final_price = price + PHOTO
    else:
        final_price = price
    print(f"Your final bill is {final_price}€")
else:
    print("Sorry, You have to grow taller before you can ride")
