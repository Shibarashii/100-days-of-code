from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox()
driver.get("https://www.python.org")
event_items = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li")

event_data = {}
for i, item in enumerate(event_items):
    time = item.find_element(By.TAG_NAME, "time").text
    description = item.find_element(By.TAG_NAME, "a").text

    event_data[i] = {time: description}

print(event_data)
