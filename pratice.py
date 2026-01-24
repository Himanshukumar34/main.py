# # add_contact() – add a new contact

# view_contacts() – display all contacts

# search_contact() – search by name or number

# update_contact() – edit an existing contact

# delete_contact() – remove a contact
def add_contact():
    name =str(input("Enter your name which you want to add :"))
    while True:
        contact=input("Enter your contact no:")
        if  len(contact) >10 or len(contact)<10:
            print("your contact no is invalid  , try again")
        elif len(contact)==10:
            with open("contact.txt","a") as f:
                f.write(name+  ":"  +contact+"\n")
            print("your contact is successfully saved ")
            break
def view_contact():
    with open("contact.txt","r") as f:
        num1=f.read()
        print("-----contact-----")
        print(num1)
def search_contact():
    name2 = input("Enter your name: ")

    with open("contact.txt", "r") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        name, contact = line.strip().split(":")
        if name2 == name:
            print("Name:", name)
            print("Contact:", contact)
            found = True
            break

    if not found:
        print("your name does not exist")
def update_contact():
    name3=str(input("Enter your name :"))
    with open("contact.txt") as f:
        alpha=f.readlines()
    found=False
    for i in alpha:
        name,contact= i.strip().split(":")
        if name3== name:
            contact2=int(input("Enter your contact :"))
            with open("contact.txt","w") as f:
                f.write()

def main():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. update_contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        # elif choice == "4":
        #   update_contact()
        # elif choice == "5":
        #    delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()


   

























































































































# # # # menu() – show options and control the program

# # # dic={}
# # # def add_contact():
# # #     name=str(input("Enter your name :")).upper()
# # #     while True:
# # #         contact=input("Enter your contact no. :")
# # #         if len(contact)>10:
# # #           print("your number is not valid")
# # #         elif len(contact)<10:
# # #           print("your number is not valid")
# # #         else:
# # #           dic[name]=contact
# # #           print("Contact add successfully")
# # #           break
# # # def view_contact():
# # #     if not dic:
# # #         print("you have not any contact now")
# # #     else:
# # #         print("----------CONTACT LIST---------")
# # #         for x,y in dic.items():
# # #            print(x,":",y)
# # # def search_contact():
# # #    search=str(input("Enter your name to search  :")).upper()
# # #    if search in dic:
# # #       num1=dic[search]
# # #       print(f" Name :{search} \n Contact :{num1}")
# # #    else:
# # #       print("your search is not in dic ")
# # # def update_contact():
# # #    name1=str(input("Enter your name which you want to update :")).upper()
# # #    if name1 in dic:
# # #       contact2=int(input("Enter your new contact: "))
# # #       dic[name1]=contact2
# # #       print("successfully update")
# # #    elif name1 not in dic:
# # #       print("your name is not find out")
   
# # # def delete_contact():
# # #    name=str(input("Enter your name  you want to delete :")).upper()
# # #    if name in dic:
# # #       dic.pop(name)
# # #       print("your contact is successfully removed ")
# # #    elif name not in dic:
# # #       print("your name is not find out  ")
# # # # Main menu-
# # # def main():
# # #     while True:
# # #         print("\n===== Contact Book =====")
# # #         print("1. Add Contact")
# # #         print("2. View Contacts")
# # #         print("3. Search Contact")
# # #         print("4. update_contact")
# # #         print("5. Delete Contact")
# # #         print("6. Exit")

# # #         choice = input("Enter your choice (1-5): ")

# # #         if choice == "1":
# # #             add_contact()
# # #         elif choice == "2":
# # #             view_contact()
# # #         elif choice == "3":
# # #             search_contact()
# # #         elif choice == "4":
# # #           update_contact()
# # #         elif choice == "5":
# # #            delete_contact()
# # #         elif choice == "6":
# # #             print("Goodbye!")
# # #             break
# # #         else:
# # #             print("Invalid choice. Please try again.")

# # # main()

   
# with open("contact.txt") as f:
#     print(f.readlines())