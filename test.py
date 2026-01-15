import json 
student_record={"name":'hiamsnhu',"class":45,"rollno":67}
def dump():
    with open("student.json","w") as file:
        json.dump(student_record,file)
def load():
     with open("student.json","r") as file:
        num3=json.load(file)
     print(num3)
while True:
    print("1. add data in json")
    print("2. read data in json")
    choice=int(input("Enter your choice:"))
    if choice==1:
        dump()
    elif choice==2:
        load()
    else:
        print("Thankyou")
        break
