def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b


while True:
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    num1=int(input("Enter your num1: "))
    num2=int(input("Enter your num2 :"))

    choice=int(input("Enter your choice: "))
    if choice==1:
        print("result",add(num1,num2))
    elif choice==2:
        print("result",subtract(num1,num2))
    elif choice==3:
        print("result",multiply(num1,num2))
    elif choice==4:
        print("result",divide(num1,num2))
    else:
        exit   