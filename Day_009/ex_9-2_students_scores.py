# This program converts their scores to grades
students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 84,
    "Neville": 62
}

students_grades = {}
for key in students_scores:
    score = students_scores[key]
    if 90 < students_scores[key] <= 100:
        students_grades[key] = 'Outstanding'
    elif 80 < students_scores[key] <= 90:
        students_grades[key] = 'Exceeds Expectations'
    elif 70 <= students_scores[key] <= 80:
        students_grades[key] = 'Acceptable'
    elif 70 > students_scores[key]:
        students_grades[key] = 'Fail'

print(students_grades)