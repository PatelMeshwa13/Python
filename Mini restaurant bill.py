food = input("Enter Food Name:" )
qty = int(input("Enter Quantity:" ))
price = float(input("Enter Price:" ))

bill = qty * price 

print("\n----- Restaurant bill -----")
print("Food:",food)
print("Quantity:",qty)
print("Price:",price)
print("Total bill=",bill)
