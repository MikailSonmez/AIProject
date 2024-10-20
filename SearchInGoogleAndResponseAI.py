from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
CHROME_DRIVER_PATH = "C:/Windows/chromedriver.exe"


# Function to initialize the Chrome driver
def initialize_driver():
    service = Service(CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (without GUI)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Function to perform a Google search
def google_search(query):
    driver = initialize_driver()
    driver.get("https://www.google.com")

    # Find the search box and enter the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Allow time for the results to load
    time.sleep(2)

    # Extract the first few search results
    results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    feedback = []

    for result in results[:5]:  # Limiting to the first 5 results
        title_element = result.find_element(By.TAG_NAME, "h3")
        link_element = result.find_element(By.TAG_NAME, "a")
        title = title_element.text
        link = link_element.get_attribute("href")
        feedback.append(f"Title: {title}\nLink: {link}\n")

    # Close the browser after the search
    driver.quit()

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
