student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
average = 0
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
    total_height += student_heights[i]
print(f'total height = {total_height}')
print(f'number os student = {len(student_heights)}')
if len(student_heights) != 0:
    average = round(total_height / len(student_heights))
print(f"average height = {average}")
