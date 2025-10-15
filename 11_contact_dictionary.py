contact = {}

def display_contact():
    print("\nName\t\tContact Number")
    for key in contact:
        print(f"{key}\t\t{contact[key]}")
    print()

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

while True:
    try:
        choice = int(input("\n1. Add new contact \n2. Search contact \n3. Display all contacts \n4. Edit contact \n5. Delete contact \n6. Exit \nEnter Your Choice: "))
    except ValueError:
        print("❌ Please enter a valid number between 1 and 6.")
        continue

    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the 10-digit mobile number: ")
        if is_valid_phone(phone):
            contact[name] = phone
            print("✅ Contact added successfully.")
        else:
            print("❌ Invalid phone number. Must be exactly 10 digits and contain only numbers.")

    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            print(f"✅ {search_name}'s contact number is {contact[search_name]}")
        else:
            print("❌ Name not found in contact book.")

    elif choice == 3:
        if not contact:
            print("📭 Contact book is empty.")
        else:
            display_contact()

    elif choice == 4:
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in contact:
            new_phone = input("Enter the new 10-digit mobile number: ")
            if is_valid_phone(new_phone):
                contact[edit_contact] = new_phone
                print("✅ Contact updated successfully.")
            else:
                print("❌ Invalid phone number. Must be exactly 10 digits and contain only numbers.")
        else:
            print("❌ Name not found in contact book.")

    elif choice == 5:
        del_contact = input("Enter the contact name to delete: ")
        if del_contact in contact:
            confirm = input(f"Are you sure you want to delete {del_contact}? (y/n): ")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                print("🗑️ Contact deleted.")
            else:
                print("⚠️ Deletion cancelled.")
        else:
            print("❌ Name not found in contact book.")

    elif choice == 6:
        print("👋 Exiting contact book. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number between 1 and 6.")
