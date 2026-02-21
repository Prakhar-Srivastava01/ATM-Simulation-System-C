import random

# Simple intents
responses = {
    "hello": ["Hi!", "Hello there!", "Hey!"],
    "hi": ["Hi!", "Hello!"],
    "how are you": ["I'm fine 😊", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!"]
}

print("Simple ChatBot is running... (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user_input:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand.")