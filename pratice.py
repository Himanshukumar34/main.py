# add_contact() – add a new contact

# view_contacts() – display all contacts

# search_contact() – search by name or number

# update_contact() – edit an existing contact

# delete_contact() – remove a contact

# menu() – show options and control the program
dic={}
def add_contact():
    name=str(input("Enter your name :"))
    while True:
        contact=input("Enter your contact no. :")
        if len(contact)>10:
          print("your number is not valid")
        elif len(contact)<10:
          print("your number is not valid")
        else:
          dic[name]=contact
          print("Contact add successfully")
          break
def view_contact():
    if not dic:
        print("you have not any contact now")
    else:
        print("----------CONTACT LIST---------")
        for x,y in dic.items():
           print(x,":",y)
def search_contact():
   search=str(input("Enter your name to search  :"))
   if search in dic:
      num1=dic[search]
      print(f" Name :{search} \n Contact :{num1}")
   else:
      print("your search is not in dic ")
def delete_contact():
   name=str(input("Enter your name  you want to delete :"))
   if name in dic:
      dic.pop(name)
      print("your contact is successfully removed ")
   elif name not in dic:
      print("your name is not find out  ")
# Main menu
def main():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

   
