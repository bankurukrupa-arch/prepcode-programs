blocked_usernames = ["admin", "root", "guest"]
username = "krupa"
if username not in blocked_usernames:
    print("username allowed")
else:
    print("username blocked")    