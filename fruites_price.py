# Add fruit

# Update price

# Display fruits & prices

users = {
    "admin": "1234",
    "user1": "pass1"
}

def add_fruits():
    user=input("Enter teacher name :")
    user1=input("Enter your id :")
    if user in users:
        print("your teacher name is already exits :")
        users[user]=user1
        print(users)
def update_fruits():
    user2=input('Enter your teacher name:')
    user3=input("Enter your id :")
    if user2 in users:
        users[user2]=user3
    else:
        print("Your teacher is already exist")
def display_fruits():
    print("your frutis and prices")


while True:
    print("1. Add prices")
    print("2.Uodate prices")
    print("3.Displa fruits and prices")


    choice=input("Enter your choice:")

    if choice=="1":
       add_fruits()
    elif choice=="2":
       update_fruits()
    else:
       display_fruits()
       print(users)
