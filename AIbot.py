id="c6f2o9"
print("=== Yohaan AI Bot ===")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("AI: Hey buddy!")
    
    elif user == "how are you":
        print("AI: I am doing great!")
    
    elif user == "what is your name":
        print("AI: I am Yohaan AI Bot.")
    
    elif user == "bye":
        print("AI: Goodbye buddy!")
        break
    
    else:
        print("AI: Sorry, I don't understand.")