books = []

# Load from file
if "books.txt" in __import__("os").listdir():
    books = open("books.txt").read().splitlines()

def save():
    open("books.txt", "w").write('\n'.join(books))

while True:
    print("\n1. Add Book  2. View All  3. Borrow Book  4. Return Book  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        b = input("Book name: ")
        books.append(b)
        save()
        print("Book added!")
    elif choice == "2":
        print("\nAvailable Books:")
        for i, b in enumerate(books, 1):
            print(f"{i}. {b}" if b else f"{i}. (Borrowed)")
    elif choice == "3":
        n = int(input("Enter book number to borrow: ")) - 1
        if 0 <= n < len(books) and books[n] != "":
            print(f"You borrowed: {books[n]}")
            books[n] = ""
            save()
        else:
            print("Book not available.")
    elif choice == "4":
        b = input("Book name to return: ")
        books.append(b)
        save()
        print("Book returned!")
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice.")