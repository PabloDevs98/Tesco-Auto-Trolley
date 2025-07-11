import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()
TESCO_EMAIL = os.getenv("TESCO_EMAIL")
TESCO_PASSWORD = os.getenv("TESCO_PASSWORD")

def login(driver):
    driver.get("https://www.tesco.com/account/en-GB/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(TESCO_EMAIL)
    driver.find_element(By.ID, "password").send_keys(TESCO_PASSWORD)
    driver.find_element(By.ID, "sign-in-form-submit-button").click()
    time.sleep(5)

def search_and_add(driver, item):
    search_box = driver.find_element(By.ID, "search-input")
    search_box.clear()
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        add_button = driver.find_element(By.XPATH, "//button[contains(., 'Add')]")
        add_button.click()
        print(f"Added: {item}")
    except:
        print(f"Failed to add: {item}")

def main():
    with open("shopping_list.txt") as f:
        items = [line.strip() for line in f if line.strip()]
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    login(driver)
    for item in items:
        search_and_add(driver, item)
        time.sleep(2)
    print("Done.")
    driver.quit()

if __name__ == "__main__":
    main()
