import mysql.connector
try:
    mydb=mysql.connector.connect(
            user="root",
            password="12qwQW?@",
            host="localhost",
            database="company_db"
    )
except Exception as obj:
    print("not connected")
else:
    print("connected")

con=mydb.cursor()

con.execute("""
        INSERT INTO employees (emp_id, emp_name, emp_address)
        VALUES (5, 'himanshu kumar', 'jaipur')
""")

mydb.commit()           # ← very important!
print("Record inserted successfully")

con.execute("SELLECT *FROM employees;")
for data in con:
    print(data)


    