password=123
a=int(input("enter password:"))
for i in range(0,3):
    if password != a:
        print("wrong password")
        password=int(input("enter password"))
    else:
        print("correct password")