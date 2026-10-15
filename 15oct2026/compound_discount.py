price = float(input())
discount = float(input())
extra = int(input())
price -= price * discount / 100
price -= extra
price("price:",price)