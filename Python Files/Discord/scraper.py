from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def scrape(link):
    driver_path = r"D:\Desktop\Data\E-commerce\Youtube\Byte\Meme\byte_Meme\Discord\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("start-maximized")
    option.add_argument("headless")

    # Create new Instance of Chrome
    driver = webdriver.Chrome(options=option)

    try:
        # Navigate to the Discord login page
        driver.get('https://discord.com/login')

        # Wait for the page to load and find the login elements
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )

        # Find the username and password input fields and enter your credentials
        username_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')

        # Enter your Discord username and password
        username_field.send_keys('armx94522@gmail.com')
        password_field.send_keys('Armxisaboss123')

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for login process to complete
        WebDriverWait(driver, 20).until(
            EC.url_changes('https://discord.com/login')
        )

        # Navigate to the desired channel
        driver.get(link)

        # Wait for the channel page to load
        time.sleep(5)

        # Scroll to load more messages
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(10):  # Adjust the range to load more messages if needed
            body.send_keys(Keys.PAGE_UP)
            time.sleep(1)

        # Wait for video elements to be present
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'video'))
        )

        # Find all video elements
        video_elements = driver.find_elements(By.TAG_NAME, 'video')

        # Create a list to store video URLs
        video_urls = []

        # Extract URLs from video elements
        for video_element in video_elements:
            video_url = video_element.get_attribute('src')
            if video_url:
                video_urls.append(video_url)

        # Load existing video URLs from the JSON file or create an empty list if the file doesn't exist
        try:
            with open('video_urls.json', 'r') as file:
                existing_video_urls = json.load(file)
        except FileNotFoundError:
            existing_video_urls = []

        # Append only the new video URLs that are not already in the existing list
        new_video_urls = [url for url in video_urls if url not in existing_video_urls]

        # Append new video URLs to the existing list
        existing_video_urls.extend(new_video_urls)

        # Write the updated video URLs back to the JSON file
        with open('video_urls.json', 'w') as file:
            json.dump(existing_video_urls, file, indent=2)
        
        # Debugging: Print the new video URLs to verify
        print("New video URLs found:", new_video_urls)

    finally:
        # Close the browser
        driver.quit()

# scrape("https://discord.com/channels/922190986413744138/1156671830162145430")
scrape("https://discord.com/channels/878900741098602536/1205372043772690444")
scrape("https://discord.com/channels/988639113248899203/988639133947818064") #Kim Wong
scrape("https://discord.com/channels/1221914909080813709/1221919254295871648") #sack