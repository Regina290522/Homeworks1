from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')
driver.find_element("id", "username").send_keys("tomsmith")
driver.find_element("id", "password").send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME,'button').click()
sleep(2)
driver.quit()
