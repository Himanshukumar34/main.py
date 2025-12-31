# ✅ Project: Username & Password System with Menu

# This project lets the user create an account, log in, and do actions using loops and conditions.
print("create your account")
username=str(input("Enter your name: "))
password=int(input("Enter your password: "))
print("your account succesfully created ")
print("log in your account")
while True:
    name=str(input("Enter your name:"))
    num1=name.capitalize()
    num2= int(input("Enter your password:"))
    if username==num1 and password==num2:
            print("valid")
            break
    else:
        print("try again")

print("your account successully log in")

print("---main menu---")
print("1. change password")
print("2.check length of your password")
print("3.logout")

# Project Idea: Text-Based ATM Machine (Advanced Loop Project)
