score = 0

# Question 1
print("1. What is the capital of Pakistan?")
print("a) Lahore  b) Karachi  c) Islamabad")
answer = input("Your answer: ")
if answer == "c":
    score += 1

# Question 2
print("2. What is 5 + 3?")
print("a) 6  b) 8  c) 10")
answer = input("Your answer: ")
if answer == "b":
    score += 1

# Question 3
print("3. Which language is used in web development?")
print("a) Python  b) HTML  c) C++")
answer = input("Your answer: ")
if answer == "b":
    score += 1

# Final Score
print("You got", score, "out of 3")
