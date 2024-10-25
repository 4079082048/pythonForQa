# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.wd = None


    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username= "admin", password= "secret")
        self.create_contact(wd, Contact(firstname= "Sofia", lastname= "Zolotova", company= "ailet", address= "Tula", mobile= "89096309913", nickname= "swallow", title= "mem"))
        self.check_and_logout(wd)


    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username= "admin", password= "secret")
        self.create_contact(wd, Contact(firstname= "", lastname= "", company= "", address= "", mobile= "", nickname= "", title= ""))
        self.check_and_logout(wd)


    def check_and_logout(self, wd):
        # return to main page, logout
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_contact(self, wd, contact):
        # create contact
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def login(self, wd, username, password):
        # login
        self.open_home_page(wd)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()


    def userName(self):
        return "admin"

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

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



if __name__ == "__main__":
    unittest.main()

