import random

# Response list
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Good! How are you?", "I'm functioning well."],
    "i am also good":["I am glad to hear that", "I'm happy to hear that"],
    "i am not doing well":["Sorry to hear that","Can I help you somehow?", "I hope you feel better soon!"],
    "what's your name": ["I'm Response.", "My name is Response.", "I am called Response"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
}

# Generate response function
def generate_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity

    # Input check
    for question, response_list in responses.items():
        if question in user_input:
            return random.choice(response_list)

    # No response match
    return "I'm not sure how to respond to that."

# Main interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = generate_response(user_input)
    print("Bot:", response)