import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    database="new",
    password="12qwQW?@",
    host="localhost"
)

print("connected")

myconn = mydb.cursor()

myconn.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    phone VARCHAR(15) NOT NULL,
    balance DECIMAL(10,2) NOT NULL
);
""")

myconn.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    type VARCHAR(20),
    amount DECIMAL(10,2),
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
""")

mydb.commit()

while True:
    print("1.Create Account")
    print("2.Deposit")
    print("3. Withdraw")
    print("4.Check Balance")
    print("5.Transaction History")
    print("Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=str(input("Enter your name: "))
        num=int(input("Enter your phone number :"))
        sql="INSERT INTO (name, phone , balance) VALUES(%s,%s,0)"
        val=name,num
        myconn.execute(sql,val)
        print("successfully saved in data")
    
    



