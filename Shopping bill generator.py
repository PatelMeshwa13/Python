product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))

total=quantity * price

print("\n----- Shopping bill -----")
print("Product Name:",product)
print("Quantity:",quantity)
print("Price:",price)
print("Total bill=",total)