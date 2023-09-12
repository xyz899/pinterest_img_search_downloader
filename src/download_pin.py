"""
  _______ _     _                       _                           _         __                 _                             _           _ _                      _         _ _         _ _ _          _____ _       _                     _                     _             _                  _           _           _            
 |__   __| |   (_)                     (_)                         | |       / _|               | |                           (_)         | | |                    | |       (_) |       | (_) |        |  __ (_)     | |                   | |                   | |           | |                | |         | |         | |           
    | |  | |__  _ ___     _ __  _   _   _ ___   _ __ ___   __ _  __| | ___  | |_ ___  _ __    __| |_   _ _ __   __ _ _ __ ___  _  ___ __ _| | |_   _  __      _____| |__  ___ _| |_ ___  | |_| | _____  | |__) | _ __ | |_ ___ _ __ ___  ___| |_    __ _ _ __   __| |   _____  _| |_ _ __ __ _  ___| |_   _ __ | |__   ___ | |_ ___  ___ 
    | |  | '_ \| / __|   | '_ \| | | | | / __| | '_ ` _ \ / _` |/ _` |/ _ \ |  _/ _ \| '__|  / _` | | | | '_ \ / _` | '_ ` _ \| |/ __/ _` | | | | | | \ \ /\ / / _ \ '_ \/ __| | __/ _ \ | | | |/ / _ \ |  ___/ | '_ \| __/ _ \ '__/ _ \/ __| __|  / _` | '_ \ / _` |  / _ \ \/ / __| '__/ _` |/ __| __| | '_ \| '_ \ / _ \| __/ _ \/ __|
    | |  | | | | \__ \  _| |_) | |_| | | \__ \ | | | | | | (_| | (_| |  __/ | || (_) | |    | (_| | |_| | | | | (_| | | | | | | | (_| (_| | | | |_| |  \ V  V /  __/ |_) \__ \ | ||  __/ | | |   <  __/ | |   | | | | | ||  __/ | |  __/\__ \ |_  | (_| | | | | (_| | |  __/>  <| |_| | | (_| | (__| |_  | |_) | | | | (_) | || (_) \__ \
    |_|  |_| |_|_|___/ (_) .__/ \__, | |_|___/ |_| |_| |_|\__,_|\__,_|\___| |_| \___/|_|     \__,_|\__, |_| |_|\__,_|_| |_| |_|_|\___\__,_|_|_|\__, |   \_/\_/ \___|_.__/|___/_|\__\___| |_|_|_|\_\___| |_|   |_|_| |_|\__\___|_|  \___||___/\__|  \__,_|_| |_|\__,_|  \___/_/\_\\__|_|  \__,_|\___|\__| | .__/|_| |_|\___/ \__\___/|___/
                         | |     __/ |                                                              __/ |                                       __/ |                                                                                                                                                    | |                             
                         |_|    |___/                                                              |___/                                       |___/                                                                                                                                                     |_|                             
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import time

def fetch_and_save_images(url, image_directory_path, num_images):
    # Setup browser
    browser = webdriver.Chrome()

    try:
        # Navigate to the URL
        browser.get(url)

        # Scroll down to load images starting from a specific position
        scroll_position = 400  # Adjust this value as needed
        browser.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(2)  # Add a short delay to allow content to load

        # Scroll down further to load remaining images
        for _ in range(10):  # You can adjust the number of times to scroll further
            browser.execute_script("window.scrollBy(0, 400);")
            time.sleep(1)

        # Wait for images to appear
        WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

        # Fetch and save images
        image_elements = browser.find_elements(By.TAG_NAME, 'img')[:num_images]
        for index, img_element in enumerate(image_elements):
            img_url = img_element.get_attribute('src')
            img_data = requests.get(img_url).content
            file_path = os.path.join(image_directory_path, f'img_{index}.jpg')
            with open(file_path, 'wb') as handler:
                handler.write(img_data)
        
        print("Images fetched and saved successfully!")

    finally:
        browser.quit()

if __name__ == "__main__":
    url = 'https://jojowiki.com/Jotaro_Kujo/Gallery'
    image_directory_path = './jotaro'
    num_images = 50
    
    if not os.path.exists(image_directory_path):
        os.makedirs(image_directory_path)
    
    fetch_and_save_images(url, image_directory_path, num_images)
