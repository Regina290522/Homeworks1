from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr/")


driver.find_element(By.XPATH,"//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
alert = driver.switch_to.alert
alert.accept()