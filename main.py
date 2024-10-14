from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Path to Edge WebDriver
service = Service(executable_path="C:\\Users\\chris\\OneDrive\\Desktop\\Selenium\\msedgedriver.exe")  # Update path

# Initialize WebDriver
driver = webdriver.Edge(service=service)

driver.get("http://localhost:3000")

# Step 1 - Wait for the element to show up (random delay added)
delay = random.uniform(2.0, 5.0)  # Delay between 2 to 5 seconds
time.sleep(delay)

# Step 2 - Wait until the username input shows up (timeout after 10 seconds)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "usernameID"))  # Replace with actual ID of the username field
)

# Step 3 - Input the username and password
input_element = driver.find_element(By.ID, "usernameID")  # Locate the username field by ID
input_element.clear()
input_element.send_keys("christo")  # Send username

input_element = driver.find_element(By.ID, "passwordID")  # Locate the password field by ID
input_element.clear()
input_element.send_keys("admin")  # Send password

# Step 4 - Click the "Login" button (replace with the correct selector for the button)
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  # Locate the button using its text
login_button.click()  # Perform the click action

# Pause to see the result (adjust or remove as needed)
time.sleep(100)

# Close the browser
driver.quit()
