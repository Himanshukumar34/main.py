num1=int(input("Enter in num1:"))
num2=str(input("kilogram/dyne/gram/hour/minute: "))


if num2=="kilogram":
    print("kilogram :",num1/1000)

elif num2=="gram" :
    print("gram :",num1*1000)

elif num2=="dyne" :
    print("dyne :",num1*100000)

elif num2=="hour":
    print("hour :", num1/60 )

elif num2=="minutes":
    print("minutes :",num1/60)