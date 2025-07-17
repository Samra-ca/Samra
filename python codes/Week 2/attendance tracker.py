import json
from datetime import date

# Load attendance data
def load_attendance():
    try:
        with open("attendance.txt", "r") as f:
            return json.load(f)
    except:
        return {}

# Save attendance data
def save_attendance(data):
    with open("attendance.txt", "w") as f:
        json.dump(data, f)

# Mark attendance for today
def mark_attendance(data):
    today = str(date.today())
    while True:
        roll = input("Enter roll number (or 'done' to finish): ")
        if roll.lower() == 'done':
            break
        if roll not in data:
            data[roll] = []
        if today not in data[roll]:
            data[roll].append(today)
    save_attendance(data)

# Show attendance percentage
def show_percentage(data):
    total_days = len(set(date for dates in data.values() for date in dates))
    if total_days == 0:
        print("No attendance data yet.")
        return
    for roll, dates in data.items():
        percent = (len(dates) / total_days) * 100
        print(f"Roll {roll}: {percent:.2f}% present")

# Main menu
attendance = load_attendance()

while True:
    print("\n1. Mark Attendance\n2. Show Attendance %\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        mark_attendance(attendance)
    elif choice == "2":
        show_percentage(attendance)
    elif choice == "3":
        break
    else:
        print("Invalid choice")