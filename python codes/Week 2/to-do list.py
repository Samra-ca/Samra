tasks = []

# Load from file
if "tasks.txt" in __import__("os").listdir():
    tasks = open("tasks.txt").read().splitlines()

while True:
    print("\n1. Add  2. View  3. Remove  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        t = input("Task: ")
        tasks.append(t)
        open("tasks.txt", "a").write(t + "\n")
        print("Added!")

    elif choice == "2":
        print("\nTo-Do List:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        n = int(input("Task number to remove: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            open("tasks.txt", "w").write('\n'.join(tasks) + '\n')
            print("Removed!")
        else:
            print("Invalid!")

    elif choice == "4":
        break

    else:
        print("Invalid choice")