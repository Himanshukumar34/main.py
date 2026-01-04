# Add, update, delete, and display student marks.
store={}
def add():
    name=str(input("Enter your name :"))
    marks =int(input("Enter your marks :"))
    store[name]=marks
    print("your record succesfully saved ")
def display():
    if not store:
        print("you have no record")
    else:
        print(store)
def update():
    name=str(input("Enter your name :"))
    if name not in  store :
        print("your name is not match ")
    marks2=int(input("Enter your marks :"))
    store[name]=marks2
    print("marks updated succsfully ")
def delete():
    name3=str(input("Enter your name which you want to delete :"))
    if name3 not in  store :
        print("your name is not match ")
    del store[name3]
    print("your recored is delted")
while True:
    print("1. add")
    print("2. display")
    print("3. update")
    print("4. deltete")
    choice=int(input("Enter your choice :"))
    if choice==1:
        add()
    elif choice==2:
        display()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    else:
        print("thanks you ")
        break
    