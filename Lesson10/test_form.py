import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from FormPage import *

@allure.title("Проверка формы")
def test_form():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    with allure.step("Заполненеие параметров"):
        main_page.input_first("Иван")
        main_page.input_last("Петров")
        main_page.input_address("Ленина, 55-3")
        main_page.input_zip("")
        main_page.input_city("Москва")
        main_page.input_country("Россия")
        main_page.input_mail("test@skypro.com")
        main_page.input_phone("+7985899998787")
        main_page.input_job("QA")
        main_page.input_company("SkyPro")
    with allure.step("Проверка результата"):
        assert 'success' in main_page.check_field("first-name")
        assert 'success' in main_page.check_field('last-name')
        assert 'success' in main_page.check_field('address')
        assert 'danger' in main_page.check_field('zip-code')
        assert 'success' in main_page.check_field('city')
        assert 'success' in main_page.check_field('country')
        assert 'success' in main_page.check_field('e-mail')
        assert 'success' in main_page.check_field('phone')
        assert 'success' in main_page.check_field('job-position')
        assert 'success' in main_page.check_field('company')
    browser.quit()