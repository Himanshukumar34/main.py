import random
password=int(input("Enter your length  password  :"))
chars="abcdefghijklmnopqurstuvwxyz12345786907$%$%*(*)+_"
# num2=random.randint(chars)
count=[]
for i in range(1,password+1):
    num3=random.choice(chars)
    count+=num3
    num4="".join(count)

print("your password is ",num4)




