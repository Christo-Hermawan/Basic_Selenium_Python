from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

import time

service = Service(executable_path="chromedriver.exe")
# drive = webdriver.Chrome(service=service)

driver = webdriver.Chrome()

driver.get("https://google.com")

# preferably

# step 1 - wait until the elements shows up

WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyF"))
)  # to wait if after 5s until the element with the class name shows up

# step 2 - then do the thing

input_element = driver.find_element(By.CLASS_NAME, "gLFyf") # find the element by class name
input_element.clear() # clear the elements incase the field not empty / have default value
input_element.send_keys("test selenium" + Keys.ENTER) # send text/input + enter 


time.sleep(10)

driver.quit()

