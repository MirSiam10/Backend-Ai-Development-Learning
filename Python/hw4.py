my_info = ["Name: Mir Siam", "Age: 23", "City: Dhaka", "Department: CSE", "Batch: 60", "Score: 90"]

print("First item:", my_info[0])
print("Last item:", my_info[-1])
print("\n")

print("Middle items:", my_info[1:-1])
print("\n")

my_info.append("Grade: A")
print("After append:", my_info)
print("\n")

my_info.remove("Score: 90")
print("After removing Score: 90:", my_info)
print("\n")

my_info.sort()
print("Sorted list:", my_info)
print("\n")

my_tuple = tuple(my_info)
print("Tuple:", my_tuple)


#my_tuple[0] = "Name: SAM"