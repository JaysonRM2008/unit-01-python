todos = [""] # Initial list of todos
while True: #Main loop
# Display current todo list
    print("Your current to-dos are: ")
# Use while loop to print each todo with a number (#)

    i = 0
    while i < len(todos):
        print(f"#{i + 1} {todos[i]}")
        i += 1
# Show a message if the list is empty
    if len(todos) == 0:
        print("[No to-dos in your list]")
        
    # Separator line for clarity
    print("\n" + "~" * 50 + "\n")

 # Ask the user what they want to do
    action = input("Would you like to add, remove, edit, clear all, or exit? ").strip().lower()

# Option to add a new todo
    if action == "add":
        new = input("What is your new to-do? ").strip()
        if new:
            todos.append(new)  # Add to list

    # Option to remove a todo by number
    elif action == "remove":
        if todos:
            try: 
                num = int(input("Which # todo would you like to remove? "))
                if 1 <= num <= len(todos):
                       todos.pop(num - 1)  # Remove the selected item
                else:
                    print("Invalid number.")
            except:
                print("Please enter a valid number.")
        else:
            print("Nothing to edit.")
 # Option to clear the entire list
    elif action == "clear all":
        todos.clear()

 # Exit the program
    elif action == "exit":
        break
    # Catch invalid inputs
    else:
        print("Invalid option.")
