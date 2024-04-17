# Write a program that adds the digits in a 2 digits number.
# e.g. if the input was 35 then the output should be 3+5 = 8
# Warning: Don not change your code on lines 1-3. Your program should work for diferentes inputs.
# e.g. any two digits number

print("--- Program add digits of a number ---")
number = input("Type a two digits number: ")
first_digit = number[0]
second_digit = number[1]
result = int(first_digit) + int(second_digit)
print(f"The summ of the digits of the number {number} are {first_digit}+{second_digit}={result}")
