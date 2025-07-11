import random
chars = "abcdeABCDE12345!@#$"
password = ""
for i in range(6):
    password += random.choice(chars)
print("Your password is:", password)