import mysql.connector
mydb=mysql.connector.connect(
     user="root",
     host="localhost",
     password="12qwQW?@",
     database="login"
)

myconn=mydb.cursor()

myconn.execute("""CREATE TABLE system(
               Userid INT UNIQUE,
               Username  VARCHAR(255),
               password VARCHAR(255),
               date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);""")
