with open("todos.txt") as files:   # Replace with open
    todos = files.read().splitlines()
print(todos)
while True:  # Main loop

    # Display current todo list
    if not todos:
        print("[No to-dos in your list]")
    else:
        print("Your list contains:")
        for i in range(len(todos)):
            print(f"#{i + 1} {todos[i]}")

    # Separator line for clarity
    print("\n" + "~" * 50 + "\n")

    # Ask the user what they want to do
    action = input("Would you like to add, remove, edit, clear all, or exit? ").strip().lower()

    # Option to add a new todo
    if action == "add":
        new = input("What is your new to-do? ").strip()
        if new:
            todos.append(new)

    # Option to remove a todo by number
    elif action == "remove":
        if todos:
            try:
                num = int(input("Which # to-do would you like to remove? "))
                if 1 <= num <= len(todos):
                    removed = todos.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Nothing to remove.")

    # Option to edit a to-do
    elif action == "edit":
        if todos:
            try:
                num = int(input("Which # to-do would you like to edit? "))
                if 1 <= num <= len(todos):
                    new_text = input("Enter the new text: ").strip()
                    if new_text:
                        todos[num - 1] = new_text
                        print("To-do updated.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Nothing to edit.")

    # Option to clear the entire list
    elif action == "clear all":
        todos.clear()
        print("All to-dos have been cleared.")

    # Exit the program
    elif action == "exit":
        print("Goodbye!")
            # Catch invalid inputs
        break
