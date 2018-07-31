from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("setUp","url")
class TestAjaxandModels():
    def test_ajaxandmodels(self,setUp,url):
        self.driver=setUp
        driver=self.driver
        driver.get(url)
        clicks = driver.find_elements_by_css_selector('.dropdown-toggle')
        for check in clicks:
            check.click()
            break
        elemCheckBoxDemo=driver.find_element_by_css_selector('a[href="./ajax-form-submit-demo.html"]')
        elemCheckBoxDemo.click()

        nametxtbox = driver.find_element_by_id('title')
        nametxtbox.send_keys("Today")
        commentbox = driver.find_element_by_id('description')
        commentbox.send_keys("Tomarrow is friday")
        submitbtn = driver.find_element_by_id('btn-submit')
        submitbtn.click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'submit-control'), "Form submited Successfully!"))
        finalcheck = driver.find_element_by_css_selector('#submit-control')
        assert "Form submited Successfully!" in finalcheck.text

