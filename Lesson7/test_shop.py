from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import *


def test_total():
    browser = webdriver.Chrome()

    Username = Registration(browser)
    Username.registr("standard_user",
                     "secret_sauce")

    main_page = MainPage(browser)
    main_page.add()

    info = Checkout(browser)
    info.info("Sergei", "Shlyapnikov", "607650")

    cart_page = CartPage(browser)
    total = cart_page.cart()

    assert total == "Total: $58.29"
    browser.quit()