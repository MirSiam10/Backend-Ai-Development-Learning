
my_cart = {
    "id": 101,
    "items": ["tomato", "meat", "egg"],
    "total_price": 4500
}

print("Cart ID:", my_cart["id"])

print("Items:", my_cart["items"])

print("First item:", my_cart["items"][0])
print("Last item:", my_cart["items"][-1])

print("First 2 items:", my_cart["items"][:2])

if "egg" in my_cart["items"]:
    print("egg is in the cart")
else:
    print("egg is not in the cart")

my_cart["items"].append("rice")

my_cart["items"].remove("tomato")

print("Number of items:", len(my_cart["items"]))

my_cart["total_price"] = 5000

print("Final cart:", my_cart)