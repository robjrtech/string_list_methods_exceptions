# This is a simple list manager program that allows the user to add, display, and remove numbers from a list.
list = []

# This program will continue to run until the user chooses to exit.
def menu():
    print("1. Add a number to the list")
    print("2. Display the list")
    print("3. Remove a number from the list")
    print("4. Exit")

# A while loop that will continue to run until the user chooses to exit.
while True:
    menu()
    choice = input("Please enter your choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        user_input = input("Please enter a number: ")
        list.append(user_input)
    elif choice == 2:
        print("The list contains:", list)
    elif choice == 3:
        user_input = input("Please enter the number you want to remove: ")
        if user_input in list:
            list.remove(user_input)
        else:
            print("Number not found in the list.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
        