# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.get("https://katalon.com/download-recorder")
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_link_text("home").click()
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("searchstring").clear()
        wd.find_element_by_name("searchstring").send_keys("sister")
        wd.find_element_by_name("searchstring").send_keys(Keys.ENTER)
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Stop'])[1]/following::div[2]").click()
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_id("content").click()
        wd.find_element_by_id("content").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Sofia")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Zolotova")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("ailet")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Tula")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("89096309913")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("swallow")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("mem")
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
