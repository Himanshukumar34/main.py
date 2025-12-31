# 1. Add Task  
# 2. View Tasks  
# 3. Remove Task  
# 4. Exit
num2=[]
def add_task():
    num1=str(input("Enter your task :"))
    num2.append(num1)
    print("your task sucessfull added")
    x="".join(num2)
def view_task():
    if not num2:
        print("no task found")
    else:
        print(f"your task is {num2}")
def remove_task():
    num3=str(input("Enter your task remove :"))
    if num3 in num2:
         num2.remove(num3)
         print("your task succesfully remove")
    else:
     print("task is not match ")
    
print("1. add task ")
print("2. View task")
print("3. Remove task ")
print("4. EXIT")

while True:
    num5=int(input("Enter your choice :"))
    if num5==1:
        add_task()
    elif num5==2:
        view_task()
    elif num5==3:
        remove_task()
    else:
        print("thanks you ")
        break