# Simple Rule-Based Chatbot
# Practical B4

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can ask me about my name, time, greetings, or say bye.")

    while True:
        user_input = input("You: ").lower()

        # Greeting
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")

        # Name
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I am a rule-based chatbot.")

        # How are you
        elif "how are you" in user_input:
            print("Chatbot: I am fine! Thank you for asking.")

        # Help
        elif "help" in user_input:
            print("Chatbot: I can respond to simple predefined questions.")

        # College
        elif "college" in user_input:
            print("Chatbot: I can help you with basic college-related queries.")

        # Thank you
        elif "thank" in user_input:
            print("Chatbot: You're welcome!")

        # Exit
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        # Unknown input
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Start chatbot
chatbot()