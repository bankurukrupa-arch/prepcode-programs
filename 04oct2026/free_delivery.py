order_amount = int(input("enter the order amount:"))
premium = True
if order_amount >=1000 or premium:
    print("free delivery")
else:
    print("delivery charges applied")    