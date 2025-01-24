# Input number of students
n = int(input())

# Input student names and grades
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Extract unique grades and find the second lowest
grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]

# Find students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Sort names alphabetically and print them
for name in sorted(second_lowest_students):
    print(name)









