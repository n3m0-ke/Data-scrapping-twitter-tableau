import csv
from getpass import getpass
from time import sleep



from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

driver = webdriver.Edge()

driver.get('https://twitter.com/FedEx')
timeout = 15
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//input[@name="text"]'))
    WebDriverWait(driver, timeout).until(element_present)
    username = driver.find_element(by=By.XPATH, value='//input[@name="text"]')
    username.send_keys('theseventhkido1')
    username.send_keys(Keys.RETURN)

    my_password = getpass()

    password = driver.find_element(by=By.XPATH, value='//input[@name="password"]')
    password.send_keys(my_password)
    password.send_keys(Keys.RETURN)    
        
    time.sleep(5)

    search_input = driver.find_element(by=By.XPATH, value = '//input[@aria-label="Search query"]')
    search_input.send_keys('FedEx')
    search_input.send_keys(Keys.RETURN)

    time.sleep(3)

    driver.find_element_by_link_text('Lates').click()




except TimeoutException:
    print ("Timed out waiting for page to load")

time.sleep(10)
try:
    driver.find_element_by_link_text('Retry').click()
except NoSuchElementException:
    print("No Such Element")

cards = driver.find_elements(by=By.XPATH, value='div[@data-testid="tweet"]')

card = cards[0]

