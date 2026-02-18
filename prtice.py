num1=int(input("Enter your num1:"))
num2=int(input("Enter your num2: "))
num3=int(input("Enter your num3:"))
if num1>num2 and num1>num3:
    print(f"max={num1}")
elif num2>num3 and num2> num1:
    print(f"max={num2}")

elif num3>num1 and num3>num2:
    print(f"max={num3}")