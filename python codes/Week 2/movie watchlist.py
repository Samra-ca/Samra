import json

# Load watchlist from file
def load_watchlist():
    try:
        with open("watchlist.txt", "r") as f:
            return json.load(f)
    except:
        return []

# Save watchlist to file
def save_watchlist(watchlist):
    with open("watchlist.txt", "w") as f:
        json.dump(watchlist, f)

# Show movies
def show_watchlist(watchlist):
    if not watchlist:
        print("No movies in your watchlist.")
    else:
        for movie in watchlist:
            print(f"{movie['title']} - {movie['genre']} - {movie['status']}")

# Main Program
watchlist = load_watchlist()

while True:
    print("\n1. Add Movie\n2. View Watchlist\n3. Remove Movie\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        title = input("Movie title: ")
        genre = input("Genre: ")
        status = input("Watched/Unwatched: ")
        watchlist.append({"title": title, "genre": genre, "status": status})
        save_watchlist(watchlist)

    elif choice == "2":
        show_watchlist(watchlist)

    elif choice == "3":
        title = input("Enter movie title to remove: ")
        watchlist = [m for m in watchlist if m['title'].lower() != title.lower()]
        save_watchlist(watchlist)

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")