import random 
num1="abcdefghijklmnopqurstuvwxyz!1234577960``~_++"
num3=int(input("Enter your password length:"))
count=[]
for i in range(num3):
    num2=random.choice(num1)
    count.append(num2)
    num5="".join(count)

print(num5)
