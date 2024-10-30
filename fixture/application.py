from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper

__author__ = 'Sofia'



class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def return_to_group_page(self):
        # return to group page
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")


    def submit_group_create(self):
        wd = self.wd
        wd.find_element(By.NAME, "submit").click()


    def open_group_page(self):
        wd = self.wd
        #wd.find_element(By.LINK_TEXT, "groups").click()
        wd.get("http://localhost/addressbook/group.php")

    def fill_group_form(self, group):
        # fill group
        wd = self.wd
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
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def create_contact(self, contact):
        # create contact
        wd = self.wd
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


    def username(self):
        wd = self.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()



