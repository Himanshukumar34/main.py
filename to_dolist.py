# # ✔ Add task
# # ✔ View tasks
# # ✔ Delete task
# # ✔ Mark as done


def add_task():
    task=str(input("Enter your task :"))
    with open("todo.txt","a",encoding="utf-8") as f :
        f.write("Task :"+task+" Pending⏳\n")
    print(f" succesfully added")

def view_task():
    with open("todo.txt","r",encoding="utf-8") as f:
        print(f.read())
    print("your task ")

def delete():
    delete_item =str(input("Enter your task of delete :"))
    with open("todo.txt", "r",encoding="utf-8") as f:
        lines = f.readlines()
    with open("todo.txt", "w",encoding='utf') as f:
        for line in lines:
            if delete_item.upper()!=line.upper().strip():
               f.write(line)


       
# def mark_done():
#     mark=str(input("Enter your task :"))
#     with open ("todo.txt","a") as f:
#         f.write(mark+"✅")
        
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
        view_task()
    elif choice ==3:
        delete()
    else:
        print("thanks you ")
        break 


