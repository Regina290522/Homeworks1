from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.CalcPage import CalcPage
from pages.CartPage import CartPage

def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.serch("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  #Используем только в видео
    to_be = result_page.add_books()