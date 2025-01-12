n = int(input())

# Initialize an empty dictionary to store student marks
student_marks = {}

# Read each student's name and marks
for _ in range(n):
    # Split input into name and three marks
    data = input().split()
    
    name = data[0]
    marks = list(map(float, data[1:]))  # Convert marks to float and store in a list
    student_marks[name] = marks
print (data)
# Read the query name
query_name = input()

# Calculate the average for the queried student
if query_name in student_marks:
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.4f}")