price1 = int(input("enter the price1:"))
price2 = int(input("enter the price2:"))
if price1 < price2:
    print("product is cheaper")
elif price1 > price2:
    print("product is more expensive")
else:
    print("both are same price")        