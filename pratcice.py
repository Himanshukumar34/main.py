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
    account_id INT PRIMARY KEY ,
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
        id=int(input("Enter your account id: "))
        name=str(input("Enter your name: "))
        num=int(input("Enter your phone number :"))
        sql="INSERT INTO accounts(account_id,name, phone , balance) VALUES(%s,%s,0);"
        val=id,name,num
        myconn.execute(sql,val)
        mydb.commit()
        print("successfully saved in data")
    elif choice == 2:
        id1 = int(input("Enter your id :"))
        amount = int(input("Enter your deposit: "))

        sql = "SELECT balance FROM accounts WHERE account_id=%s"
        myconn.execute(sql, (id1,))
        data = myconn.fetchone()

        if not data:
          print("Account not found")
        else:
            old_balance = data[0]
            new_balance = old_balance + amount

            sql2 = "UPDATE accounts SET balance=%s WHERE account_id=%s"
            myconn.execute(sql2, (new_balance, id1))

            sql3 = "INSERT INTO transactions (account_id, type, amount) VALUES (%s, %s, %s)"
            myconn.execute(sql3, (id1, "Deposit", amount))

            mydb.commit()
            print("Successfully saved your transaction")
    elif choice==3:
        id2=int(input("Enter your account_id:"))
        wiht=int(input("Enter your withdraw amount:"))
        sql="SELECT balance FROM accounts WHERE account_id=%s"
        values=id2
        myconn.execute(sql,values) 
        data=myconn.fetchone() 

        if not data:
            print("account not found")
        else:
            old=data[0] 
            if old_balance>wiht:
                newbalance=old_balance-wiht
            elif old_balance<wiht:
                print("you have not enough money ")
        # sql3=becontinue



