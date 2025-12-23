from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/brave"
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)
select_lang = driver.find_element(By.ID, "langSelect-EN")
select_lang.click()

time.sleep(3)
big_cookie = driver.find_element(By.ID, "bigCookie")

while True:
    big_cookie.click()
    cookie_count = driver.find_element(
        By.ID, "cookies").text.split()[0].strip()

    grandma_price = driver.find_element(By.ID, "productPrice1").text

    if int(cookie_count) > int(grandma_price):
        driver.find_element(By.ID, "product1").click()
