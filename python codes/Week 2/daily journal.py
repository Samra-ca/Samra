# Load old entries
journal = {}
try:
    with open("journal.txt", "r") as file:
        for line in file:
            date, entry = line.strip().split(":", 1)
            journal[date] = entry
except FileNotFoundError:
    pass

# Menu
print("1. Write a new journal entry")
print("2. Read journal by date")
print("3. Search by keyword")
choice = input("Enter choice (1/2/3): ")

if choice == "1":
    date = input("Enter date (dd-mm): ")
    text = input("Write your journal: ")
    journal[date] = text
    with open("journal.txt", "a") as file:
        file.write(date + ":" + text + "\n")
    print("Entry saved!")

elif choice == "2":
    date = input("Enter date (dd-mm): ")
    if date in journal:
        print("Entry on", date + ":", journal[date])
    else:
        print("No entry found.")

elif choice == "3":
    word = input("Enter keyword to search: ")
    found = False
    for date, entry in journal.items():
        if word.lower() in entry.lower():
            print(f"🔎 {date}: {entry}")
            found = True
    if not found:
        print("No matching entry.")

else:
    print("Invalid choice")