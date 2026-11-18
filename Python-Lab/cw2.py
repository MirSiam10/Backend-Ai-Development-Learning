
students = {
    "Rahim": "78",
    "Salma": "92",
    "Karim": "35",
    "Nila": "64"
}

total = 0
max_marks = 0
max_student = ""

for student, marks in students.items():
    num_marks = int(marks)
    total += num_marks
    if num_marks > max_marks:
        max_marks = num_marks
        max_student = student

average = total / len(students)
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Highest marks: {max_marks}")
print(f"Student with highest marks: {max_student}")


passed_students = []
for student, marks in students.items():
    if int(marks) >= 40:
        passed_students.append(student)
print(f"Students who passed: {passed_students}")

def get_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

for student, marks in students.items():
    grade = get_grade(int(marks))
    print(f"{student}: {marks} - Grade: {grade}")











    # Probelm:
# students = {
#     "Rahim": "78",
#     "Salma": "92",
#     "Karim": "35",
#     "Nila": "64"
# }
# 1) Calculate the total marks, average marks
# 2) Find the highest marks and the student who scored it
# 3)Make a list of only the students who passed (40 or more)
# 4) Write a function get_grade(marks) that resturns the grade and use it in