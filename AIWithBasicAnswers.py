import random

# Memory to store user's name and preferences
memory = {}


# Function to get a random response
def get_random_response(responses):
    return random.choice(responses)


# Function to greet the user and remember their name
def greet_user():
    if 'name' not in memory:
        name = input("AI Chatbot: Hi there! What's your name? ")
        memory['name'] = name
        print(f"AI Chatbot: Nice to meet you, {name}!")
    else:
        print(f"AI Chatbot: Welcome back, {memory['name']}!")


# Main chatbot function
def chatbot():
    greet_user()
    print("AI Chatbot: How can I assist you today?")

    while True:
        user_input = input(f"{memory['name']}: ").lower()

        # Responses based on common inputs
        if "hello" in user_input or "hi" in user_input:
            responses = [
                "Hello! How are you doing today?",
                "Hi there! What can I do for you?",
                "Hey! How can I assist you?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "how are you" in user_input:
            responses = [
                "I'm just a program, but I'm doing well! How about you?",
                "I'm doing fine, thanks for asking! What about you?",
                "As an AI, I'm always functional! How can I help you today?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "your name" in user_input:
            print(f"AI Chatbot: My name is simply AI, but I like to assist!")

        elif "my name" in user_input:
            print(f"AI Chatbot: Your name is {memory['name']}, right?")

        elif "weather" in user_input:
            responses = [
                "I can't check the weather, but it might be sunny somewhere!",
                "If I had access to weather data, I'd let you know!",
                "I can't look outside, but I hope it's pleasant!"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        # More elif conditions for expanded topics
        elif "hobby" in user_input or "hobbies" in user_input:
            responses = [
                "I enjoy helping people learn and chat! What about you?",
                "As an AI, my hobby is processing data! What's yours?",
                "I don't have hobbies like humans, but I love assisting!"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "food" in user_input:
            responses = [
                "I don't eat, but I hear pizza is great! What's your favorite food?",
                "If I could taste, I'd probably like pasta! How about you?",
                "Food is fascinating! Do you have a favorite cuisine?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "favorite color" in user_input:
            responses = [
                "As an AI, I don't see colors, but blue seems calming!",
                "I think green represents growth and knowledge. What's yours?",
                "Color is subjective, but I'd say yellow symbolizes positivity!"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "travel" in user_input or "vacation" in user_input:
            responses = [
                "I'd love to visit all corners of the world if I could!",
                "Travel is amazing! Do you have a favorite destination?",
                "Vacations sound fun! Where would you go on a dream vacation?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "game" in user_input:
            responses = [
                "I don't play games, but I've heard chess is a great challenge!",
                "Gaming sounds fun! What's your favorite game?",
                "I wonder what it's like to play video games. Do you have a favorite?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "music" in user_input:
            responses = [
                "Music is such a universal language! What type do you enjoy?",
                "I've heard classical music can be very soothing! What do you listen to?",
                "I can't hear music, but I know it's powerful! Do you have a favorite genre?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "movie" in user_input or "film" in user_input:
            responses = [
                "Movies are so creative! Do you have a favorite genre?",
                "I can't watch films, but I've heard sci-fi is really imaginative! What's your favorite?",
                "If I could watch movies, I'd probably enjoy something futuristic. How about you?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "sport" in user_input:
            responses = [
                "Sports are exciting! Do you play any?",
                "I don't play sports, but football seems to be very popular. What's your favorite?",
                "Which sport do you like to watch or play?"
            ]
            print(f"AI Chatbot: {get_random_response(responses)}")

        elif "bye" in user_input or "goodbye" in user_input:
            print(f"AI Chatbot: Goodbye, {memory['name']}! Have a great day!")
            break

        else:
            fallback_responses = [
                "I'm sorry, could you rephrase that?",
                "I don't quite understand, can you ask something else?",
                "Hmm, I don't know about that, but feel free to ask anything else."
            ]
            print(f"AI Chatbot: {get_random_response(fallback_responses)}")


# Run the expanded chatbot
chatbot()
