'''Problem 1
Print the numbers from 1 to 15, each on a new line.

Problem 2
Take a number from the user and print its multiplication table (1 to 10).
Example: 5 x 1 = 5, 5 x 2 = 10 ...

Problem 3
Calculate the sum of all numbers from 1 to 50 using a for loop.

Problem 4
You have this list: [12, 7, 25, 40, 33, 18]
Use a for loop to print only the even numbers, and also print how many even numbers there are.

Problem 5
Use this dictionary:
marks = {"math": 80, "english": 65, "science": 90}
Using a for loop, print each subject with its marks, then print the total and the average.'''
# Code for Problem 1
for i in range(1, 16):
    print(i)

# Code for Problem 2
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Code for Problem 3

total = 0

for i in range(1, 51):
    total += i

print("Total sum:", total)

# Code for Problem 4
numbers = [12, 7, 25, 40, 33, 18]

count = 0

for num in numbers:
    if num % 2 == 0:
        print(num)
        count += 1

print("Total even numbers:", count)

# Code for Problem 5
marks = {"math": 80, "english": 65, "science": 90}

total = 0

for subject, score in marks.items():
    print(subject, ":", score)
    total += score

print("Total marks:", total)
print("Average marks:", total / len(marks))