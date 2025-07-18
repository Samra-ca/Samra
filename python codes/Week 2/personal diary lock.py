PASSWORD = "1234" 

def login():
    pwd = input("Enter password: ")
    return pwd == PASSWORD

def write_entry():
    entry = input("Write your diary entry:\n")
    with open("diary.txt", "a") as f:
        f.write(entry + "\n---\n")
    print("Entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r") as f:
            print("\nYour Diary:\n")
            print(f.read())
    except FileNotFoundError:
        print("No entries yet.")

# Main
if login():
    while True:
        print("\n1. Write Entry\n2. Read Diary\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            break
        else:
            print("Invalid option.")
else:
    print("Wrong password! Access denied.")