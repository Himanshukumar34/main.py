# todo list in python
dic={}
def add_task():
    num1=int(input("how many task you add: "))
    for i in range(1,num1):  
        task=str(input("Enter your task :")).upper()
        dic[i]=task
    print("your task is successfully added")
def view_task():
    if not dic:
        print("you have no task this time ")
    else:
        print("your task is ")
        for key,value in dic.items():
            print(key ,":" ,value)
def delete_task():
    task1=str(input("which task you want to delete  :"))
    if task1.upper() in dic:
       del dic[task1]
       print("your task is successfully delete")
    else:
        print("this task has not exists")
while True:
    print("1. add task \n 2. view task \n 3. delete task \n 4. exit")
    choice =int(input("Enter your choice:"))
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        delete_task()
    else:
        print(" thanks you ")
        break           
            



