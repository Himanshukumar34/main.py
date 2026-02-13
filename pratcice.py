# Add student
# View all students
# Search student
# Update marks
# Delete student
# Show topper
# Exit
num1=[]
def add_student():
    student=str(input("Enter student name :"))
    roll_num=int(input("Enter your roll num :"))
    marks1=int(input("Enter your marks in hindi:"))
    marks2=int(input("Enter your marks in english :"))
    marks3=int(input("Enter your student in math :"))
    num1.append(f"""Name= {student} hindi= {marks1} english= {marks2}  math=  { marks3} Roll={roll_num}""")
    print("record saved in data ")
def view_all_student():
    if not num1:
        print("NO found student record")
    else:
        print("----STUDENT RECORD-----")
        for i in num1:
            print(i)
        

def search_student():
    num2=int(input("Enter roll num which you want to see:"))
    for i in num1:
        if i.strip()==f"Roll={num2}":
            print(i[0],i[1],i[2],i[3],i[4])
            
# def update_marks():
       
while True:
    print("---------student management system ------")
    print("1. Add student")
    print("2. View student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.show student")
    print("7.Exit ")
    choice=int(input("Enter your choice ;"))
    if choice==1:
        add_student()
    elif choice==2:
        view_all_student()
    elif choice==3:
        search_student()

