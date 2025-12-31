# Add new books

# Borrow & return

# Track available books

# Store book list in a file

def add_book():
    book=str(input("Enter your book :"))
    with open("student.txt","a") as f:
        f.write(f"your book is {book}\n"
                f"----------------")
        print("successfully added ")

def track():
    book1=str(input("Enter your book :"))
    with open("student.txt") as f:
       line= f.readlines()
    with open("syudent.txt","w") as f:
       for lines in line:
           if lines!=book1:
               print("your book is not exists ")
       else: 
           f.write(line)
print("your file is retrun")
def view():
    with open("student.txt","r") as f:
        print(f.read())

while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_book()
    elif choice==2:
       track()
    elif choice==3:
        view()
    else:
        break