# 🍃🍀
import random

# Function to greet the user
def greet():
    responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    return random.choice(responses)

# Function to provide a response based on user input
def respond(input_text):
    input_text = input_text.lower()
    
    if "hello" in input_text or "hi" in input_text or "hey" in input_text:
        return greet()
    elif "your name" in input_text or "who are you" in input_text:
        return "I am an AI assistant. How can I help you?"
    elif "bye" in input_text or "goodbye" in input_text:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that command."

# Main function to run the AI assistant
def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        else:
            response = respond(user_input)
            print("Assistant:", response)

if __name__ == "__main__":
    main()
# written by Pratham 🍂🍁 