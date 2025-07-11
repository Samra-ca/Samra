print(" Welcome to the Word Guessing Game!")
secret_word = "programming"
guessed = ["_"] * len(secret_word)
attempts = 6
while attempts > 0 and "".join(guessed) != secret_word:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ")
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed[i] = guess
        print(" Correct!")
    else:
        attempts -= 1
        print(" Wrong! Attempts left:", attempts)

if "".join(guessed) == secret_word:
    print("\n Congratulations! You guessed the word:", secret_word)
else:
    print("\n Out of attempts! The word was:",secret_word)