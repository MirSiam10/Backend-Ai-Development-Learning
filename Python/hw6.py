
colors = {"red", "blue", "green", "red", "blue"}
print("1. Colors:", colors)
print("Type:", type(colors))


numbers = [1, 2, 2, 3, 3, 4]
numbers_set = set(numbers)
print("\n2. Numbers set:", numbers_set)


fruits = {"apple", "banana", "mango", "orange"}
print("\n3. Fruits:", fruits)
print("Length:", len(fruits))


set_a = {"apple", "banana", "mango"}
set_b = {"mango", "orange", "banana"}


print("\n4. Union:", set_a | set_b)


print("5. Intersection:", set_a & set_b)

# 6. Difference (set_a - set_b)
print("6. Difference:", set_a - set_b)


text = "hello"
unique_characters = set(text)
print("\n7. Unique characters:", unique_characters)


emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print("\n8. Unique emails:", unique_emails)
print("Number of unique emails:", len(unique_emails))
