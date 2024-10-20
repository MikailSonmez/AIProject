from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.DEBUG)

# Function to initialize the Chrome WebDriver
def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()  # Maximize the window
    return driver

# Function to ask a question on the AI site
def ask_question(driver, site_url, question):
    driver.get(site_url)

    try:
        # Wait for the input box to be visible (update the XPath according to the site's structure)
        input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type your question']"))  # Adjust as needed
        )
        input_box.send_keys(question)

        # Locate and click the send button (update the XPath according to the site's structure)
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send')]"))  # Adjust as needed
        )
        send_button.click()  # Click the send button

        # Wait for the response to be visible (update the XPath according to the site's structure)
        response = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='response-class']"))  # Adjust as needed
        )
        return response.text

    except Exception as e:
        print(f"Error while interacting with {site_url}: {e}")
        return None

# Main function to orchestrate the querying
def main():
    question = input("Enter your question: ")
    sites = {
        "ChatGPT": "https://chat.openai.com/",
        "Claude": "https://claude.ai/",
        "Jasper": "https://www.jasper.ai/",
        "Cohere": "https://cohere.ai/",
        "Bing AI": "https://www.bing.com/chat",
        # Add more AI model sites as needed
        "Google Bard": "https://bard.google.com/",
        "DeepAI": "https://deepai.org/",
        "Copy.ai": "https://www.copy.ai/",
        "Writesonic": "https://writesonic.com/",
        "Kuki": "https://www.kuki.ai/",
        "Replika": "https://replika.ai/",
        "YouChat": "https://you.com/chat",
        "Turing": "https://www.turing.com/",
        "Character AI": "https://character.ai/",
        "Botpress": "https://botpress.com/",
        "EleutherAI": "https://www.eleuther.ai/",
        # Continue adding other AI platforms...
    }

    driver = initialize_driver()
    feedback = {}

    for model, url in sites.items():
        print(f"Querying {model}...")
        response = ask_question(driver, url, question)
        feedback[model] = response if response else "No response received."

    driver.quit()

    print("\nFeedback on AI responses:\n")
    for model, response in feedback.items():
        print(f"{model} Response: {response}\n")

# Run the main function
if __name__ == "__main__":
    main()
