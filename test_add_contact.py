# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.get("https://katalon.com/download-recorder")
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_link_text("add new").click()
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_link_text("home").click()
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("searchstring").clear()
        driver.find_element_by_name("searchstring").send_keys("sister")
        driver.find_element_by_name("searchstring").send_keys(Keys.ENTER)
        driver.find_element_by_id("content").click()
        driver.find_element_by_name("add").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_name("to_group").click()
        driver.find_element_by_name("to_group").click()
        driver.find_element_by_name("add").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Stop'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("content").click()
        driver.find_element_by_id("content").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Sofia")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Zolotova")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("ailet")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Tula")
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("89096309913")
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("swallow")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("mem")
        driver.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
