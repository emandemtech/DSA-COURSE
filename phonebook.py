# phonebook project with search/update/delete
phonebook = {}
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact {name} added with number {number}.")
def search_contact(name):
    if name in phonebook:
        print(f"Contact {name} found with number {phonebook[name]}.")
    else:
        print(f"Contact {name} not found.")
def update_contact(name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"Contact {name} updated with new number {number}.")
    else:
        print(f"Contact {name} not found. Cannot update.")
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found. Cannot delete.")
def display_contacts():
    if phonebook:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")
