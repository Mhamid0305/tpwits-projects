import json
import os

FILE_NAME = "contacts.json"


# === Utility Functions ===

def read_data():
    """Reads contact list from the JSON file."""
    if not os.path.isfile(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def write_data(data):
    """Writes updated contact list to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)


# === Contact Book Functionalities ===

def create_contact():
    """Prompts user to input and add a new contact."""
    print("\n📥 Add New Contact")
    name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")

    contact = {"name": name, "phone": phone, "email": email}
    all_contacts = read_data()
    all_contacts.append(contact)
    write_data(all_contacts)

    print("✅ Contact has been saved successfully!\n")


def list_contacts():
    """Displays all saved contacts."""
    contacts = read_data()
    if not contacts:
        print("📭 No contacts found.\n")
        return

    print("\n📃 Saved Contacts:")
    for index, person in enumerate(contacts, 1):
        print(f"{index}. Name: {person['name']} | Phone: {person['phone']} | Email: {person['email']}")
    print()


def find_contact():
    """Searches for a contact using name or phone number."""
    query = input("🔍 Enter name or phone number to search: ")
    contacts = read_data()
    matches = [c for c in contacts if c['name'] == query or c['phone'] == query]

    if matches:
        print("\n✅ Match Found:")
        for match in matches:
            print(f"Name: {match['name']}, Phone: {match['phone']}, Email: {match['email']}")
        print()
    else:
        print("❌ No contact found with that information.\n")


def modify_contact():
    """Updates name and email of a contact using phone number as identifier."""
    phone_to_update = input("📞 Enter phone number of the contact to update: ")
    contacts = read_data()

    for contact in contacts:
        if contact['phone'] == phone_to_update:
            print("✏️ Editing contact...")
            contact['name'] = input("Updated Name: ")
            contact['email'] = input("Updated Email: ")
            write_data(contacts)
            print("✅ Contact has been updated.\n")
            return

    print("⚠️ No contact with that phone number was found.\n")


def remove_contact():
    """Deletes a contact by phone number."""
    phone_to_delete = input("🗑️ Enter phone number to remove: ")
    contacts = read_data()
    new_list = [c for c in contacts if c['phone'] != phone_to_delete]

    if len(new_list) == len(contacts):
        print("❌ No contact found to delete.\n")
    else:
        write_data(new_list)
        print("🧹 Contact deleted successfully.\n")


# === Application Loop ===

def main_menu():
    while True:
        print("========== 📞 CONTACT BOOK ==========")
        print("1. Add a Contact")
        print("2. Show All Contacts")
        print("3. Search for a Contact")
        print("4. Edit a Contact")
        print("5. Delete a Contact")
        print("6. Exit the Program")

        choice = input("➡️ Choose an option (1-6): ").strip()

        if choice == '1':
            create_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            find_contact()
        elif choice == '4':
            modify_contact()
        elif choice == '5':
            remove_contact()
        elif choice == '6':
            print("👋 Thank you for using Contact Book. Goodbye!\n")
            break
        else:
            print("⚠️ Invalid option. Please enter a number from 1 to 6.\n")


# === Run the Application ===

if __name__ == "__main__":
    main_menu()
