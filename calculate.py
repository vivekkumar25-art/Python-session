
item1 = float(input("Enter first item price: ₹"))
item2 = float(input("Enter second item price: ₹"))

subtotal = item1 + item2
discount = subtotal * 15 / 100
delivery_fee = 99
final_total = subtotal - discount + delivery_fee

print("\n----- MYNTRA BILL -----")
print(f"First item: ₹{item1:.2f}")
print(f"Second item: ₹{item2:.2f}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Promo discount (15%): -₹{discount:.2f}")
print(f"Delivery fee: ₹{delivery_fee:.2f}")
print(f"Final total: ₹{final_total:.2f}")
