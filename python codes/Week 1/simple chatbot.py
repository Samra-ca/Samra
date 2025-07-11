print("---AI Chatbot---")
while True:
    user_input=input("You: ").lower()
    if user_input=="hello":
        print("Bot: hello! ")
    elif user_input=="how are you?":
        print("Bot: I am good.")
    elif user_input=="can you help me in doing my work?":
        print("Bot: yes, sure i am here to help you")
    elif user_input=="bye":
        print("Bot: Bye")
        break
    else:
        print("Invalid input")