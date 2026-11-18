# # First Part: 
# students = {
#     "Rahim": "78",
#     "Salma": "92",
#     "Karim": "35",
#     "Nila": "64"
# }


# print("Student marks:")
# for name, marks in students.items():
#     print(f"{name}: {marks}")
#     # Second Part:
#     if int(marks) >= 80:
#         print("Grade: A+")

#     if int(marks) >= 60 and int(marks) < 79:
#         print("Grade: B")

#     if int(marks) >= 40 and int(marks) < 59:
#         print("Grade: B")

#     if int(marks) < 40:
#         print("Grade: F")

# # Find total marks and average marks and Highest marks


# # total_marks = sum(int(marks) for marks in students.values())
# # average_marks = total_marks / len(students)
# # highest_marks = max(int(marks) for marks in students.values())

# total =0
# max_marks = 0
# name= ""
# n=0

# for name, marks in students.items():
#     total += int(marks)
#     if int(marks) > max_marks:
#         max_marks = int(marks)
#         highest_student = name

# average = total / len(students)

# print(f"\nTotal Marks: {total}")
# print(f"Average Marks: {average}")
# print(f"Highest Marks: {max_marks} by {name}")




students = {
    "Rahim": "78",
    "Salma": "92",
    "Karim": "35",
    "Nila": "64"
}

# PART 1: Print student marks and grades

print("Student Marks and Grades:")

for name, marks in students.items():
    print(f"\n{name}: {marks}")

    if int(marks) >= 80:
        print("Grade: A+")
    elif int(marks) >= 60:
        print("Grade: B")
    elif int(marks) >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")


# PART 2: Calculate total, average and highest marks

total = 0
max_marks = 0

# IMPORTANT: Use a separate variable for the highest student's name
highest_student = ""

for name, marks in students.items():

    total += int(marks)

    if int(marks) > max_marks:
        max_marks = int(marks)
        highest_student = name

average = total / len(students)


print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Marks: {max_marks} by {highest_student}")

