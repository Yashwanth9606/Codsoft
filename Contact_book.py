import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    keyword = input("Enter name or phone to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            print("Leave blank to keep existing value.")
            name = input(f"New name ({contacts[idx]['name']}): ") or contacts[idx]['name']
            phone = input(f"New phone ({contacts[idx]['phone']}): ") or contacts[idx]['phone']
            email = input(f"New email ({contacts[idx]['email']}): ") or contacts[idx]['email']
            address = input(f"New address ({contacts[idx]['address']}): ") or contacts[idx]['address']

            contacts[idx] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"Contact '{removed['name']}' deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    contacts = load_contacts()

    while True:
        print("\n📒 CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
