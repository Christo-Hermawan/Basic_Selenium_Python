from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# path to Edge WebDriver
service = Service(executable_path="chromedriver.exe")

# initialize WebDriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.bing.com")

# step 1 - Wait for the element to show up (random delay added)
delay = random.uniform(2.0, 5.0)  # Delay between 2 to 5 seconds
time.sleep(delay)

# step 2 - wait until the elements shows up
# wait if after 10s until the element with the class name shows up
# if the element doesn't show, shut the program
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sb_form_q"))
)

# step 3 - then do the activity
input_element = driver.find_element(By.ID, "sb_form_q") # find the element by class name
input_element.clear() # clear the elements incase the field not empty / have default value
time.sleep(delay)
input_element.send_keys("youtube" + Keys.ENTER) # send text/input + enter 


# if the link text to exist then continue
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "YouTube"))
)

time.sleep(delay)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube")
link.click();

time.sleep(50)

driver.quit()

