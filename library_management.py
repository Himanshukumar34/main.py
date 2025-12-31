# Add student data
# Update marks
# Display topper
# Save records permanently
print("----Student card management system ------")
dic={}
def add_student():
    student=str(input("Enter your name :"))
    marks=int(input("Enter your marks  :"))


    dic[student]=[marks]
    print(dic)

def update():
    student=str(input("Enter your name :"))
    if student in dic:
        marks=int(input("Enter your marks :"))
        dic[student]=marks
        print("your marks successfully updated")

def topper():
    if not dic:
        print("no student you fill ")
    else:
        topper=max(dic,dic.get)
        print(f"your topper is {topper}")
def show():
    if not dic:
        print("no student found")
    else:
        print(f"your all student record is {dic}")
print("1.Add student data")
print("2.Update marks")
print("3.Display topper ")
print(" 4.Save records permanently")
while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        add_student()
        
    elif choice==2:
        update()
        
    elif choice==3:
        topper()
    else:
        show()
    