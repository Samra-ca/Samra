expenses = []
try:
    file = open("expenses.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        expense = {"date": parts[0], "category": parts[1], "amount": float(parts[2])}
        expenses.append(expense)
    file.close()
except FileNotFoundError:
    pass  # file will be created later

# Show total spent
total = 0
for e in expenses:
    total += e["amount"]
print("Total Spent: Rs.", total)

# Monthly limit
limit = 5000
if total > limit:
    print("Warning: You have crossed your monthly limit!")

# Add a new expense
date = input("Enter date (dd-mm): ")
category = input("Enter category (e.g. food, travel): ")
amount = float(input("Enter amount: "))

# Save to list and file
new_expense = {"date": date, "category": category, "amount": amount}
expenses.append(new_expense)

file = open("expenses.txt", "a")
file.write(date + "," + category + "," + str(amount) + "\n")
file.close()

print("Expense added!")