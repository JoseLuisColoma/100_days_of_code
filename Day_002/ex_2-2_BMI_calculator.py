# BMI Calculator
# Write a program that calculates the Body Mass Index (BMI) from a user´s weight and height
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

print("--- BMI Calculator ---")
weight = int(input("Type your Weight (in kg.): "))
height = float(input("Type your height (in m.): "))
bmi = weight / (height ** 2)

print(round(bmi, 2))


