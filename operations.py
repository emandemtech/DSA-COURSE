from phonebook import add_contact, search_contact, delete_contact, update_contact, display_contacts

while True:

    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == "2":
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter contact name to update: ")
        number = input("Enter new contact number: ")
        update_contact(name, number)
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Phonebook.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")