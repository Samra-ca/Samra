import json

FILENAME = "habits.json"

# Load existing data
try:
    with open(FILENAME, "r") as f:
        habits = json.load(f)
except FileNotFoundError:
    habits = {}

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(habits, f)

def log_habit():
    habit = input("Enter habit name: ")
    habits[habit] = habits.get(habit, 0) + 1
    print(f"Logged '{habit}'. Total: {habits[habit]}")
    save_data()

def view_habits():
    if not habits:
        print("No habits tracked yet.")
    else:
        for habit, count in habits.items():
            print(f"{habit}: {count} times")

# Menu
while True:
    print("\n1. Log Habit\n2. View Progress\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        log_habit()
    elif choice == "2":
        view_habits()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
