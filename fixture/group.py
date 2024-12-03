from tokenize import group

from selenium.webdriver.common.by import By
from model.group import Group
__author__ = 'Sofia'

class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None

    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()


    def create(self, group):
        self.fill_form(group)
        self.submit_creation()
        self.group_cache = None


    def submit_creation(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()


    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        self.group_cache = None #?

    def fill_group_form(self, group):
        wd = self.app.wd
        #self.open_group_page()
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)
        #self.group_cache = None


    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
        #self.group_cache = None


    def del_first_group(self):
        self.del_group_by_index(0)

    def del_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.open_group_page()
        self.group_cache = None

    def del_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.open_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" %id).click()

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open form
        wd.find_element(By.NAME, "edit").click()
        # fill
        self.fill_group_form(new_group_data)
        # submit
        wd.find_element(By.NAME, "update").click()
        self.open_group_page()


    def count_g(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None: #if cache is empty - load
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache) #back copy list