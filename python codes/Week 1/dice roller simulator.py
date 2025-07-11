import random
while True:
    user=input("Press enter or roll a dice ")
    if user=="q":
        break
    dice=random.randint(1,6)
    print(dice)