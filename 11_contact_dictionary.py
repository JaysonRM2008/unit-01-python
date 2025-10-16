# Dictionary to store contact name as key and phone number as value
contact = {}

# Function to display all contacts in a formatted way
def display_contact():
    print("\nName\t\tContact Number")
    for key in contact:
        print(f"{key}\t\t{contact[key]}")
    print()

# Function to validate if the phone number is exactly 10 digits and numeric
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Main loop to show menu and take user input repeatedly
while True:
    try:
        # Display menu and get user choice
        choice = int(input("\n1. Add new contact \n2. Search contact \n3. Display all contacts \n4. Edit contact \n5. Delete contact \n6. Exit \nEnter Your Choice: "))
    except ValueError:
        # Handle invalid input that cannot be converted to int
        print("Please enter a valid number between 1 and 6.")
        continue

    if choice == 1:
        # Add new contact
        name = input("Enter the contact name: ").strip()  # Remove extra spaces
        phone = input("Enter the 10-digit mobile number: ").strip()
        if is_valid_phone(phone):
            contact[name] = phone  # Save contact
            print("Contact added successfully.")
        else:
            print("Invalid phone number. Must be exactly 10 digits and contain only numbers.")

    elif choice == 2:
        # Search for a contact by name
        search_name = input("Enter the contact name to search: ").strip()
        if search_name in contact:
            print(f"{search_name}'s contact number is {contact[search_name]}")
        else:
            print("Name not found in contact book.")

    elif choice == 3:
        # Display all contacts if any exist
        if not contact:
            print("Contact book is empty.")
        else:
            display_contact()

    elif choice == 4:
        # Edit existing contact's phone number
        edit_contact = input("Enter the contact name to edit: ").strip()
        if edit_contact in contact:
            new_phone = input("Enter the new 10-digit mobile number: ").strip()
            if is_valid_phone(new_phone):
                contact[edit_contact] = new_phone  # Update phone number
                print("Contact updated successfully.")
            else:
                print("Invalid phone number. Must be exactly 10 digits and contain only numbers.")
        else:
            print("Name not found in contact book.")

    elif choice == 5:
        # Delete a contact
        del_contact = input("Enter the contact name to delete: ").strip()
        if del_contact in contact:
            confirm = input(f"Are you sure you want to delete {del_contact}? (y/n): ")
            if confirm.lower() == 'y':
                contact.pop(del_contact)  # Remove contact from dictionary
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Name not found in contact book.")

    elif choice == 6:
        # Exit the program
        print("Exiting contact book. Goodbye!")
        break

    else:
        # Handle choices outside the valid range
        print("Invalid choice. Please enter a number between 1 and 6.")
