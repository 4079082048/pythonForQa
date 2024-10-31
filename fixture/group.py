
from selenium.webdriver.common.by import By
__author__ = 'Sofia'

class GroupHelper():
    def __init__(self, app):
        self.app = app


    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")


    def submit_creation(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "submit").click()


    def open_group_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def fill_form(self, group):
        # fill group
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "group_name").click()


    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

