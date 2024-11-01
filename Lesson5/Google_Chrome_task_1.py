from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    driver.find_element(By.XPATH,"//button[text()='Add Element']").click()

delete_buttons = driver.find_elements("xpath", "//button[text()='Delete']")
print(f"Количество кнопок Delete: {len(delete_buttons)}")
