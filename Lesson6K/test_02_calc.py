import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configparser import *

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text() = '7']").click()
    driver.find_element(By.XPATH, "//span[text() = '+']").click()
    driver.find_element(By.XPATH, "//span[text() = '8']").click()
    driver.find_element(By.XPATH, "//span[text() = '=']").click()

    result = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    result_text = driver.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"
