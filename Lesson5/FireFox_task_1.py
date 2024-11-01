from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)
close_button = driver.find_element("xpath", "//div[@class='modal-footer']/p[text()='Close']")
close_button.click()
driver.quit()