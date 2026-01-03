num1 = []

while True:
    try:
        print("------- Todo List ------")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter your task: ")
            num1.append(task)
            print("Your task is successfully added")

        elif choice == 2:
            task2 = input("Enter task to remove: ")
            if task2 in num1:
                num1.remove(task2)
                print("Task removed successfully")
            else:
                print("Task not found")

        elif choice == 3:
            print("Your tasks are:", num1)

        elif choice == 4:
            print("Thank you")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Your value is wrong")

            