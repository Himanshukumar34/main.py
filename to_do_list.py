def add_task():
    task=str(input("Enter your task :"))
    with open("task.txt","a") as f:
        f.write(f"task :{task}\n")
        print("added succefully ")
def view():
    with open("task.txt","r") as f:
        view=f.read()
        print(f"{view}")
def delete():
    delete=str(input("Enter your task:"))
    with open("task.txt","r") as f:
        line=f.readlines() 
    with open("task.txt","w")as f:
        for lines in line:
            if lines.strip()!=line:
                f.write(lines)     
            else:
                print("task not exists")
        print("your task successfuly added")
while True:
    print("Welcome to do list")
    print("1. add task ")
    print("2. view task ")
    print("3. delete task")
    print("4. marks as done")

    choice =int(input("Enter your choice :"))
    if choice ==1:
        add_task()

    elif choice==2:
        view()
    elif choice ==3:
        delete()
    else:
        print("thanks you")
        break

