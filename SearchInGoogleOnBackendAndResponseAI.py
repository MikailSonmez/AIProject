import requests

# Replace with your API key and Search Engine ID
API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"


# Function to perform a Google search using the API
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
    }

    response = requests.get(url, params=params)
    search_results = response.json()

    feedback = []
    if "items" in search_results:
        for item in search_results['items'][:5]:  # Get top 5 results
            title = item['title']
            link = item['link']
            snippet = item.get('snippet', 'No description available')
            feedback.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n")
    else:
        feedback.append("No results found.")

    return feedback


# Main function for the AI to interact with the user
def ai_search_bot():
    print("AI Search Bot: Hello! What would you like to search for?")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input or "exit" in user_input:
            print("AI Search Bot: Goodbye! Have a nice day!")
            break
        else:
            print(f"AI Search Bot: Searching for '{user_input}'...")
            results = google_search(user_input)
            print("AI Search Bot: Here are the top results:\n")
            for result in results:
                print(result)
            print("\nWhat else would you like to search for?")


# Run the AI search bot
ai_search_bot()
