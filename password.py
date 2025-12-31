import random
num1= int(input("Enter your length of password :"))
chars="abcdefghijklmnopqurstuvwxyz123456778990-=!@#$%^&*()_+|"
password=""

for i in range(num1):
    choice=random.choice(chars)
    password+=choice
print(f"your password  :",password)
        
