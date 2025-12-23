from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(
#     By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Pages")
# # all_portals.click()

# try:
#     search_button = driver.find_element(By.CLASS_NAME, "search-toggle")
#     search_button.click()
# except:
#     pass

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Hello")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("World")

email = driver.find_element(By.NAME, "email")
email.send_keys("Helloworld@gmail.com")

signup_button = driver.find_element(By.CLASS_NAME, "btn")
signup_button.click()
