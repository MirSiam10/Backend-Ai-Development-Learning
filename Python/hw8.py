# Problem 1:-----------------------------------------
number = 10
while number >= 1:
    print(number)
    number -= 1
print("Blast off!")
# Problem 2:--------------------------------------------
secret_word = ""
while secret_word != "python":
    secret_word = input("Enter the secret word: ")
print("Access Granted")
# Problem 3:--------------------------------------------
def calculate_bill(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.05
    total = subtotal + tax
    return total
result = calculate_bill(100, 3)
print("Final Bill:", result)
# Problem 4:--------------------------------------------
def cube(n):
    return n * n * n
def sum_of_cubes(a, b):
    result = cube(a) + cube(b)
    return result
answer = sum_of_cubes(2, 3)
print("Sum of cubes:", answer)
# Problem 5:--------------------------------------------
def find_average(*numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        print("Please provide at least one number.")
        return
    average = total / count
    print("Average:", average)
find_average(10, 20, 30)
# Problem 6:--------------------------------------------
def student_id(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
student_id(
    name="Siam",
    roll=101,
    section="A"
)