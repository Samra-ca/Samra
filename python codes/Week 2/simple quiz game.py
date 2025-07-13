# Quiz Questions (Question, Answer)
quiz = [
    ("What is the capital of Pakistan?", "islamabad"),
    ("2 + 2 = ?", "4"),
    ("What is the color of the sky?", "blue"),
    ("Python is a ___ language.", "programming"),
    ("How many days in a week?", "7")
]

score = 0

# Load highest score
high_score = 0
if "score.txt" in __import__("os").listdir():
    f = open("score.txt", "r")
    high_score = int(f.read())
    f.close()

print("🎮 Welcome to the Quiz Game!\n")

# Ask questions
for q, ans in quiz:
    user_ans = input(f"{q} ").strip().lower()
    if user_ans == ans:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {ans}\n")

print(f"Your Score: {score}/{len(quiz)}")

# Update high score if beaten
if score > high_score:
    print("New High Score!")
    f = open("score.txt", "w")
    f.write(str(score))
    f.close()
else:
    print(f"Highest Score: {high_score}")