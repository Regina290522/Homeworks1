from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Явное ожидание: ждать появления элемента с текстом "SkyPro"
element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "SkyPro"))
    )
