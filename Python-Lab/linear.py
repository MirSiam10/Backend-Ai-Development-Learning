contact_list = ["Siam", "Sifat", "Punno"]

target = input("Enter the Target: ")

size_contact = len(contact_list)
result = 0
for i in range(size_contact):

    if(target == contact_list[i]):

        result = i
        break
    else:
        result =-1

if result == -1:
    print("Result not found")
else:
    print(f"Result {target} is found at index {result}")


