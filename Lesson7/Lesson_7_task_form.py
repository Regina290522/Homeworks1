from Form.Pages.FormPage import FormPage
from Form.Pages.DataPage import DataPage
from selenium import webdriver
driver = webdriver.Chrome()

def test_form():
    form_page = FormPage()
    form_page.find_types()
    form_page.data_entry()
    form_page.click_button()

    data_page = DataPage()
    data_page.find_types()
    data_page.atribut_class_fn()
    data_page.atribut_class_ln()
    data_page.atribut_class_address()
    data_page.atribut_class_mail()
    data_page.atribut_class_phone()
    data_page.atribut_class_zip()
    data_page.atribut_class_city()
    data_page.atribut_class_country()
    data_page.atribut_class_job()
    data_page.atribut_class_company()

    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(By.ID, "company").get_attribute("class")