print("Welcome to AI-BUDDY Chatbot!!")
print("You can ask me basic questions and if you type BYE then exit from the bot")

# chatbot memory creation (store keys in lowercase for easy matching)
responses = {
    "hello": "Hi, welcome to this chatbot. How can I help you?",
    "how are you?": "I am very good, thank you for asking.",
    "what is your name?": "I am smart AI-BUDDY, your personal assistance.",
    "what can you do for me?": "I can help you solve basic questions and also do basic calculations.",
    "motivate me": "Keep going, you are never give up at any moment, you can do it.",
    "happy": "Great to hear that and you can do your best things.",
    "sad": "Don't worry, it's okay to feel sad sometimes. Just try to do something that makes you happy.",
}

# method to get response from chatbot
def get_responsesofbot(user_question: str) -> str:
    user_question = user_question.strip().lower()

    for key, value in responses.items():
        if key in user_question:
            return value

    return "I didn't understand that. Please ask something else."

# take user input
while True:
    user_Input = input("Please ask your questions: ").strip()

    if "bye" in user_Input.lower():
        print("AI-BUDDy: Goodbye!")
        break

    reply = get_responsesofbot(user_Input)
    print("AI-BUDDy:", reply)

   

