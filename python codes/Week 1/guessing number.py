import random
randomNum=random.randrange(1,5)
guessedNum=int(input("Enter any number between 1 and 5 to guess: "))
while randomNum!=guessedNum:
    guessedNum=int(input("Again enter number between 1 and 5 to guess: "))
else:
    print("Your guess is correct. The number is: ")
    print(randomNum)