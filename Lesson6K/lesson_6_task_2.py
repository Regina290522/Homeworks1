from selenium import webdriver
from selenium.webdriver.common.by import By


# используем Google Chrome.
# переименовать на кнопку
driver = webdriver.Chrome()

#переходим на страницу
driver.get("http://uitestingplayground.com/textinput")

#находим поле ввода и пишем в нем текст SkyPro:
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

#нажимаем на синюю кнопку:
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

#получаем текст кнопки и выводим в консоль:
button_name = driver().find_element(By.CSS_SELECTOR, "#updatingButton").text
print(f"Текст кнопки: {button_name}")

driver.quit()