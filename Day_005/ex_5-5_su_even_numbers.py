# Type a number between 1 and 1000
target = int(input())
even_sum = 0
for number in range (2, target + 1, 2):
    even_sum += number

print(even_sum)
