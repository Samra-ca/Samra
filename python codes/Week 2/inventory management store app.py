inv = {}

# Load from file
if "inv.txt" in __import__("os").listdir():
    for line in open("inv.txt"):
        name, qty = line.strip().split(",")
        inv[name] = int(qty)

def save():
    open("inv.txt", "w").write('\n'.join([f"{k},{v}" for k, v in inv.items()]))

while True:
    print("\n1. Add  2. View  3. Update  4. Remove  5. Out of Stock  6. Exit")
    c = input("Choose: ")

    if c == "1":
        name = input("Product: ")
        qty = int(input("Qty: "))
        inv[name] = qty
        save()
        print("Added!")
    elif c == "2":
        for name, qty in inv.items():
            print(f"{name} - {'Out of Stock' if qty == 0 else qty}")
    elif c == "3":
        name = input("Product to update: ")
        if name in inv:
            inv[name] = int(input("New Qty: "))
            save()
            print("Updated!")
        else:
            print("Not found.")
    elif c == "4":
        name = input("Remove product: ")
        if name in inv:
            del inv[name]
            save()
            print("Removed!")
        else:
            print("Not found.")
    elif c == "5":
        print("Out of Stock:")
        for name, qty in inv.items():
            if qty == 0:
                print(name)
    elif c == "6":
        break
    else:
        print("Invalid")