item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the quantity: "))

subtotal = item_price * item_quantity
vat = subtotal * 0.05
service_charge = subtotal * 0.10

print(f"""Subtotal Price: {subtotal}
VAT: {vat}
Service Charge: {service_charge}""")

result = subtotal + vat + service_charge
print(f"Total price : {result:.2f}")

