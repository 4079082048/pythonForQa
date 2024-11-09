
from selenium.webdriver.common.by import By
__author__ = 'Sofia'

class GroupHelper:
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
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)


    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    #def open_home_page(self):
    #    wd = self.app.wd
    #    wd.get("http://localhost/addressbook/index.php")

    def del_first_group(self):
        wd = self.app.wd
        #self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.open_group_page()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #open form
        wd.find_element(By.NAME, "edit").click()
        #fill
        self.fill_group_form(new_group_data)
        #submit
        wd.find_element(By.NAME, "update").click()
        self.open_group_page()


    def count_g(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

