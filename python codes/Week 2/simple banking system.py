import json

FILENAME = "accounts.json"

# Load accounts from file
try:
    with open(FILENAME, "r") as f:
        accounts = json.load(f)
except FileNotFoundError:
    accounts = {}

def save_accounts():
    with open(FILENAME, "w") as f:
        json.dump(accounts, f)

def create_account():
    acc = input("Enter account number: ")
    pin = input("Set a 4-digit PIN: ")
    if acc in accounts:
        print("Account already exists.")
    else:
        accounts[acc] = {"pin": pin, "balance": 0}
        save_accounts()
        print("Account created!")

def login():
    acc = input("Account number: ")
    pin = input("PIN: ")
    if acc in accounts and accounts[acc]["pin"] == pin:
        return acc
    else:
        print("Invalid account or PIN.")
        return None

def deposit(acc):
    amt = float(input("Amount to deposit: "))
    accounts[acc]["balance"] += amt
    print("Deposited successfully.")
    save_accounts()

def withdraw(acc):
    amt = float(input("Amount to withdraw: "))
    if accounts[acc]["balance"] >= amt:
        accounts[acc]["balance"] -= amt
        print("Withdrawn successfully.")
    else:
        print("Insufficient balance.")
    save_accounts()

def check_balance(acc):
    print(f"Balance: Rs {accounts[acc]['balance']}")

# Menu
while True:
    print("\n1. Create Account\n2. Login\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        user = login()
        if user:
            while True:
                print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Logout")
                c = input("Choose: ")
                if c == "1":
                    deposit(user)
                elif c == "2":
                    withdraw(user)
                elif c == "3":
                    check_balance(user)
                elif c == "4":
                    break
                else:
                    print("Invalid option.")
    elif choice == "3":
        break
    else:
        print("Invalid option.")
