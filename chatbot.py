responses = {
    "hello": "Hi there! What's on your mind today?",
    "lahore": "The cultural heart of Punjab! The history and food streets there are truly unmatched.",
    "cricket": "The Pakistani national team always brings incredible passion and energy to the pitch!",
    "help": "I can chat with you about basic topics. Try saying hello, asking about cricket, or typing exit.",
    "bye": "Goodbye! Have a fantastic day."
}

print("System: AI Chatbot Initialized. Type 'exit' to quit.\n")

while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    
    if clean_input == "exit":
        print("Bot: Shutting down the logic engine. Goodbye!")
        break
        
    reply = responses.get(clean_input, "I do not understand.")
    print(f"Bot: {reply}")