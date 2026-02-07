import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    password="12qwQW?@",
    database="contact",
    user="root"
)
print("connected")
myconn=mydb.cursor()
myconn.execute("""
     CREATE TABLE krishna(
               id INT PRIMARY KEY,
               name VARCHAR(255),
               phone INT NOT NULL,
               Email VARCHAR(255),
               Address VARCHAR(255)
);""")

while True:
    print("1. Add contact")
    print("2. View contact")
    print("3. search contact")
    print("4. update contact ")
    print("5. delete contact")
    choice=int(input("Enter your choice  :"))
    if choice ==1:
         name=str(input("Enter your name :")).strip()
         phone =int(input("Enter your phone number :")).strip()
         email=input("Enter your email :").strip()
         address=str(input("Enter your address :")).strip()
         num2="INSERT INTO krishna(name,phone,Email,Address), VALUES(%s,%s,%s,%s)"
         num1=(name,phone,email,address)
         myconn.execute(num2,num1)
         mydb.commit()
         print("your task is successfully created ")
        