from selenium.webdriver.common.by import By
from model.contact import Contact
__author__ = 'Sofia'


class ContactHelper():
    def __init__(self, app):
        self.app = app



    def create(self, new_contact_data):
        # create contact
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.get("http://localhost/addressbook/edit.php")
        self.fill_contact_data(new_contact_data)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()



    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def del_first_contact(self):
        self.del_contact_by_index(0)
        self.contact_cache = None

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.contact_cache = None

    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        #self.app.open_home_page()
        self.select_first_contact()
        # edit contact
        wd.find_element(By.XPATH, "//a/img[@title='Edit']/parent::a").click()
        self.fill_contact_data(new_contact_data)
        #submit contact update
        wd.find_element(By.NAME, 'update').click()
        self.contact_cache = None


    def fill_contact_data(self, contact):
        #wd = self.app.wd
        self.change_filed_value("firstname", contact.firstname)
        self.change_filed_value("lastname", contact.lastname)
        self.change_filed_value("company", contact.company)
        self.change_filed_value("address", contact.address)
        self.change_filed_value("mobile", contact.mobile)
        self.change_filed_value("nickname", contact.nickname)
        self.change_filed_value("title", contact.title)
        self.contact_cache = None

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)
