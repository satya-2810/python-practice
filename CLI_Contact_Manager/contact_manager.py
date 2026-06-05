import json
import os

def add_contact(contacts):
    name = input("Enter the name of your contact: ").strip()
    if not name:
        print("Invalid Input: Description cannot be blank")
        return
    phone = input("Enter the phone number: ").strip()
    if not phone.isdigit():
        print("Invalid Input: Phone number must only contain numbers")
        return
    if len(phone)!=10:
        print("Invalid Input: Phone number must be of 10 digits")
        return
    email = input("Enter the email: ").strip()
    if '@' not in email:
        print("Invalid Input: Email is invalid")
        return
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added Successfully!")
  
def view_contacts(contacts):
    if not contacts:
        print("Contact List is Empty")
    else:
        print(f"{'Name':<12} {'Phone Number':<15} {'email':<20}")
        
        for row in contacts:
            print(f"{row['name']:<12} {row['phone']:<15} {row['email']:<20}")
            
def search_contact(contacts):
    if not contacts:
        print("Contact List is empty")
    else:
        try:
            option = int(input("Enter how you want to search \n1. Search by name \n2. Search by number\n"))
            if option==1:
                req_name = input("Enter the name: ")
                found=False
                for contact in contacts:
                    if req_name == contact["name"]:
                        print(f"{'Name':<12} {'Phone Number':<15} {'email':<20}")
                        print(f"{contact['name']:<12} {contact['phone']:<15} {contact['email']:<20}")
                        found=True
                if not found:
                    print("Contact Not Found!")
            elif option==2:
                req_number = input("Enter the number: ")
                found = False
                for contact in contacts:
                    if req_number == contact["phone"]:
                        print(f"{'Name':<12} {'Phone Number':<15} {'email':<20}")
                        print(f"{contact['name']:<12} {contact['phone']:<15} {contact['email']:<20}")
                        found = True
                if not found:
                    print("Contact Not Found!")
            else:
                print("Invalid Input: Input should either be 1 or 2")
        except ValueError:
            print("Invalid Input: Input must be a number")

def delete_contact(contacts):
    if not contacts:
        print("Contact List is empty")
    else:
        name_to_delete = input("Enter the name of the contact you want to delete: ")
        found = False
        for index, contact in enumerate(contacts):
            if name_to_delete == contact["name"]:
                found = True
                contacts.pop(index)
                save_contacts(contacts)
                print("Contact Deleted Successfully")
                break
        if not found:
            print("No Contact Found!")
        
def load_contacts():
    if os.path.exists("contacts.json"):
        file = open("contacts.json", 'r')
        contacts = json.load(file)
        file.close()
        return contacts
    else:
        return []

def save_contacts(contacts):
    file = open("contacts.json", 'w')
    json.dump(contacts, file, indent=2)
    file.close()


contacts = load_contacts()
while True:
    try:
        choice = int(input("Enter the operation you want to perform: \n1. Add Contact \n2. View Contacts \n3. Search Contact \n4. Delete Contact\n5. Quit\n"))
        if choice==1:
            add_contact(contacts)
        elif choice==2:
            view_contacts(contacts)
        elif choice==3:
            search_contact(contacts)
        elif choice==4:
            delete_contact(contacts)
        elif choice==5:
            print("Thank You!")
            break
        else:
            print("Invalid Input: Input must be between 1 to 5")
    except ValueError:
        print("Invalid Input: Input must be a number")