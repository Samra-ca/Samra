def encrypt(text):
    # Caesar cipher: shift letters by 3
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - 3)
    return result

# Load existing passwords
passwords = {}
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            site, enc_pass = line.strip().split(",")
            passwords[site] = enc_pass
except FileNotFoundError:
    pass

# Menu
print("1. Save new password")
print("2. Retrieve password")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    site = input("Enter website name: ")
    pwd = input("Enter password: ")
    enc = encrypt(pwd)
    passwords[site] = enc
    with open("passwords.txt", "a") as file:
        file.write(site + "," + enc + "\n")
    print("Password saved!")

elif choice == "2":
    site = input("Enter website name to find password: ")
    if site in passwords:
        print("Password:", decrypt(passwords[site]))
    else:
        print("Not found!")
else:
    print("Invalid choice")