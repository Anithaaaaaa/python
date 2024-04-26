password=123
a=int(input("enter password"))
for i in range(0,3):
   if password!=a:
      print("wrong password")
      a=int(input("enter the password again"))
   else:
      print("correct password")

