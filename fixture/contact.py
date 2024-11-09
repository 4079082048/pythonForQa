from selenium.webdriver.common.by import By

__author__ = 'Sofia'


class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def create(self, new_contact_data):
        # create contact
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        self.fill_contact_data(new_contact_data)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    pass


    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def del_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, '[value="Delete"]')
        self.check_main_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # edit contact
        wd.find_element(By.XPATH, "//a/img[@title='Edit']/parent::a").click()
        self.fill_contact_data(new_contact_data)
        #submit contact update
        wd.find_element(By.NAME, 'update').click()
        self.check_main_page()

    def fill_contact_data(self, contact):
        #wd = self.app.wd
        self.change_filed_value("firstname", contact.firstname)
        self.change_filed_value("lastname", contact.lastname)
        self.change_filed_value("company", contact.company)
        self.change_filed_value("address", contact.address)
        self.change_filed_value("mobile", contact.mobile)
        self.change_filed_value("nickname", contact.nickname)
        self.change_filed_value("title", contact.title)
        

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))