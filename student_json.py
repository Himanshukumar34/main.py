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
          json.dumps(dic,file)
    print("student record save succesfully ")
def view_students():
    with open("stu.json","r") as file:
        view=json.loads(file)
        print(view)
def roll_num():
     roll=int(input("Enter your roll number :"))
    #  be continue