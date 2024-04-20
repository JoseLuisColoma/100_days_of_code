import sys
print("Welcome to Python Pizza Deliveries!")
PIZZA_L = 25
PIZZA_M = 20
PIZZA_S = 15
bill = 0
COST_EXTRA_PEPPERONI_S = 2
COST_EXTRA_PEPPERONI_M_L = 3
COST_EXTRA_CHEESE = 1
print("Welcome to Python Pizza Deliveries!")
print("---Choose the size of any Pizza---")
size = input("What kind of pizza do you want (L/M/S): ").upper()
if size == 'L':
    print(f"Pizza large. It costs {PIZZA_L}€")
    bill = PIZZA_L
elif size == 'M':
    print(f"Pizza Medium. It costs {PIZZA_M}€")
    bill = PIZZA_M
elif size == 'S':
    print(f"Pizza Small. It costs {PIZZA_S}€")
    bill = PIZZA_S
else:
    print("Wrong Size. The order is cancelled.")
    sys.exit()
print("---Extra ingredients---")
add_peppeoni = input("add pepperoni? (Y/N): ").upper()
add_extra_cheese = input("add extra cheese? (Y/N): ").upper()
if add_peppeoni == 'Y':
    if size == 'S':
        bill = bill + COST_EXTRA_PEPPERONI_S
    else:
        bill = bill + COST_EXTRA_PEPPERONI_M_L
if add_extra_cheese == 'Y':
    bill = bill + COST_EXTRA_CHEESE

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is ${bill}.")