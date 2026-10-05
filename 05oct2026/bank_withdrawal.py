balance = int(input("enter the balance:"))
amount = int(input("enter the amount:"))
if amount <=balance and amount % 500 == 0:
    print("transaction allowed")
else:
    print("transaction not allowed")    