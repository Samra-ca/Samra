contacts = []

if "contacts.txt" in __import__("os").listdir():
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone, email = line.strip().split(",")
            contacts.append({"name": name, "phone": phone, "email": email})

while True:
    print("\n1. Add Contact  2. Search  3. Show All  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        with open("contacts.txt", "a") as f:
            f.write(f"{name},{phone},{email}\n")
        print("Contact added!")

    elif choice == "2":
        query = input("Search by name, phone or email: ").lower()
        found = False
        for c in contacts:
            if query in c["name"].lower() or query in c["phone"] or query in c["email"].lower():
                print(f"{c['name']} | Phone: {c['phone']} | Email: {c['email']}")
                found = True
        if not found:
            print("No contact found.")

    elif choice == "3":
        print("\nAll Contacts:")
        for c in contacts:
            print(f"{c['name']} | {c['phone']} | {c['email']}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")