# A dictionary in Python is a collection of key-value pairs. 
# A dictionary is unordered, changeable, and indexed.
# In Python, dictionaries are written with curly brackets {}.

#Example of a dictionary and its use
#A dictionary to store contacts (name and phone number)
contacts = {}

# You can access the items of a dictionary by referring to its key name inside square brackets [].
# You can add a new item by using a new index key and assigning a value to it.
def add_contact():
    name = input("Enter contact's name: ")
    if name in contacts:
        print(f"A contact '{name}' already exists.")
    else:
        number = input("Enter contact's phone number: ")
        contacts[name] = number
        print(f"Contact '{name}' added")

# Using the get() method is a safer way to access values.
def lookup_contact():
    name = input("Enter the name of the contact to look up: ")
    number = contacts.get(name, "Contact not found.")
    print(f"Phone number: {number}")

#Looping through all key-value pairs
def display_contacts():
    if not contacts:
        print("Your contact book is empty.")
        return
    print("\n--- All Contacts ---")
    for name, number in contacts.items():
        print(f"Name: {name}, Phone Number: {number}")

# The del keyword removes the item with the specified key name.
def remove_contact():
    name = input("Enter name of the contact to be removed: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact {name}")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. Look up a contact")
    print("3. Display all contacts")
    print("4. Remove a contact")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        lookup_contact()
    elif choice == 3:
        display_contacts()
    elif choice == 4:
        remove_contact()
    elif choice == 5:
        print("Exiting the contact book.")
        break
    else:
        print("Enter valid input")