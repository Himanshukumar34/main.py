# ✅ Project: Username & Password System with Menu

# This project lets the user create an account, log in, and do actions using loops and conditions.
print("create your account")
username=str(input("Enter your name: ")).upper().strip()
password=int(input("Enter your password: "))
gmail=str(input("Enter your gmail  :"))
print("your account succesfully created ")
print("log in your account")
while True:
    name=str(input("Enter your name:")).upper().strip()
    num2= int(input("Enter your password:"))
    if username==name and password==num2:
            print("valid")
            break
    else:
        print("try again")

print("your account successully log in")

print("---main menu---")
print("1. change password")
print("2.check length of your password")
print("3.logout")

while True:
     user=int(input("chose any one :"))
     if user == 1:
          


