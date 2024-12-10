from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def cart(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
        print(total)
        return(total)

class Checkout:

    def __init__(self, browser):
        self._driver = browser

    def info(self, term1, term2, term3):
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name.input_error.form_input').send_keys(term1)
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name.input_error.form_input').send_keys(term2)
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code.input_error.form_input').send_keys(term3)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

class MainPage:
    def __init__(self, browser):
        self._driver = browser

    def add(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]').click()


        self._driver.find_element(By.CSS_SELECTOR, 'a[class=shopping_cart_link]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button#checkout.btn.btn_action.btn_medium.checkout_button ').click()

class Registration:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def registr(self, term, term_1):
        Username = self._driver.find_element(By.CSS_SELECTOR, 'input#user-name.input_error.form_input')
        Username.clear()
        Username.send_keys(term)

        Password = self._driver.find_element(By.CSS_SELECTOR, 'input#password.input_error.form_input')
        Password.clear()
        Password.send_keys(term_1)
        self._driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click()