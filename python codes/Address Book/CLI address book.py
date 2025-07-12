address_book={}
def add_contact():
    name=input("Name: ")
    phone=input("Phone: ")
    email=input("Email: ")
    address_book[name]={"phone":phone, "email":email}
    print("Contact added successfully!")
    
def show_contacts():
    for name, info in address_book.items():
        print(f"{name}: Phone={info['phone']}, Email={info['email']}")

def search_contact():
    name=input("Enter name to search: ")
    if name in address_book:
        print(address_book[name])
    else:
        print("Contact not found.")
while True:
    print("\n1. Add Contact\n2. Show All\n3. Search\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice")