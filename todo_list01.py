print("1. Add task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Exit")
list=[]
while True:
    user=int(input("Enter your choice"))
    if user==1:
        name=str(input("Enter your task:"))
        list.append(name)
        print(name,"your task added successfully")
    elif user==2:
        print(list)
    elif user==3:
        name2=str(input("Enter your remove"))
        list.remove(name2)
        print(name2,"your task remove successfully")
    elif user=="exit":
        print("thanks you")
        break
