# Add student details
# Store data in JSON file
# View all students
# Search student by roll number
import json
def add_student():
    dic={}
    dic["Name"]=str(input("Enter your name: "))
    dic["class"]=input("Enter your class: ")
    dic["rollno"]=int(input("Enter your roll no"))
    with open("stu.json","a") as file:
          json.dump(dic,file)
    print("student record save succesfully ")
def view_students():
    with open("stu.json","r") as file:
        view=json.load(file)
        print(view)

def roll_num():
     roll=int(input("Enter your roll number :"))
     with open("stu.json","r") as file:
          num2= json.load(file)
     if roll in num2:
          print(num2)
     elif  roll not in num2:
          print("your roll number is not find out ")
while True:
     print("1. add_student")
     print("2. view stduent")
     print("3. roll_num")
     choice=int(input("Enter your choice; "))
     if choice==1:
          add_student()
     elif choice==2:
          view_students()
     elif choice==3:
          roll_num()
     else:
          print("you enter wrong choice:  ")