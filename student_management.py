print("1. Add student record")
print("2. View all record ")
print("3. Exit")

coint=""

while True:
    user_choice=int(input("Enter your choice "))
    if user_choice==1:
        name=str(input("Enter your name :"))
        roll_num=int(input("Enter your roll num:"))
        marks1=int(input("Enter your marks in scinece: "))
        marks2=int(input("Enter your marks in math: "))
        marks3=int(input("Enter your marks in chemcistry"))
        num3=marks1+marks2+marks3
        num4=(num3/300)*100
        if num4>90 :
            num5="A"
        if num4<90 and num4>80:
            num5="B"
        if num4<80 and num4>60:
            num5="C"
        if num4<70 and num4>50:
            num5="D"
        if num4<50:
            num5="fail"
    elif user_choice==2:
        print("Name:",name)
        print("roll num",roll_num)
        print("marks in scince:",marks1)        
        print("marks in math:",marks2) 
        print("marks in chemistry:",marks3)
        print("total marks is:",num3)
        print("pecentage:",num4)
        print("Grade:",num5)

    else:
        print("thanks ")
        break