# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element(By.LINK_TEXT, "group page").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")

    def submit_group_create(self, wd):
        wd.find_element(By.NAME, "submit").click()

    def open_group_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, wd, group):
        # fill group
        self.open_group_page(wd)
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "group_name").click()
        self.return_to_group_page(wd)

    def login(self, wd, userName, password):
        #  login
        self.open_home_page(wd)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(userName)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    @property
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def test_add_group(self):
        wd = self.wd
        self.login(wd, userName="admin", password="secret")
        self.fill_group_form(wd, Group(name= "Group1",header= "header", footer= "footer"))
        self.submit_group_create(wd)


    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, userName="admin", password="secret")
        self.fill_group_form(wd, Group(name= "",header= "", footer= ""))
        self.submit_group_create(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
