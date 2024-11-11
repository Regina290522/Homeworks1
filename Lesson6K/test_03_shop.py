import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Тест
def test_01_form(driver):
    driver.get("https://www.saucedemo.com/")

first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
first_name.send_keys("Regina")

last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
last_name.send_keys("Faizova")

postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys('420047')

driver.find_element(By.CSS_SELECTOR, "#continue").click()


total_price = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

print(total_price)
