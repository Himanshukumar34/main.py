# Features:
# Add products
# Generate bill
# Update stock
# Save sales
# Tables:
# products
# sales
import mysql
mydb=mysql.connector.connect(
    user="root",
    password="12qwQW?@",
    host="localhost",
    database="sales"

)

print("connected")
myconn=mydb.connect()

myconn.execute("""CREATE TABLE product(
               product_id AUTOINCREMENT,
               name VARCHAR(255),
               price int,
               quantity VARCHAR(255)
)""")
myconn.execute("""CREATE TABLE sales(
               sale_id INT PRIMARY KEY,
               total_amount int,
               date_time DATETIME,
)""")

while True:
    print("1. add product")
    print("2. generate bill")
    print("3. update stock")
    print("4. save sales")
    print("5. exit")
    choice=int(input("Enter your choice :"))
    if choice ==1:
        name=str(input("Enter your name :"))
        price=int(input("Enter your price:"))
        quantity=int(input("Enter your quantity :"))
        sql="INSERT INTO (name, price, quantity) VALUES(%s,%s,%s)"
        values=(name,price,quantity)
        myconn.execute(sql,values)
        mydb.commit()
        print("Successfully data saved ")
    elif choice ==2:
        