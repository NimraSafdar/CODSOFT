class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.store_name} | {self.phone_number}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.store_name or query in contact.phone_number]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found!")

    def update_contact(self, store_name, updated_contact):
        for index, contact in enumerate(self.contacts):
            if contact.store_name == store_name:
                self.contacts[index] = updated_contact
                return True
        return False

    def delete_contact(self, store_name):
        for contact in self.contacts:
            if contact.store_name == store_name:
                self.contacts.remove(contact)
                return True
        return False


manager = ContactManager()

while True:
    print("\n Contact Manager ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        store_name = input("Enter store name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(store_name, phone_number, email, address)
        manager.add_contact(contact)
        print("Contact added successfully!")

    elif choice == '2':
        manager.view_contacts()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        manager.search_contact(query)

    elif choice == '4':
        store_name = input("Enter store name of the contact you want to update: ")
        print("Enter updated details:")
        new_store_name = input("Enter store name: ")
        new_phone_number = input("Enter phone number: ")
        new_email = input("Enter email: ")
        new_address = input("Enter address: ")
        updated_contact = Contact(new_store_name, new_phone_number, new_email, new_address)
        if manager.update_contact(store_name, updated_contact):
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == '5':
        store_name = input("Enter store name of the contact you want to delete: ")
        if manager.delete_contact(store_name):
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == '6':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice!")

