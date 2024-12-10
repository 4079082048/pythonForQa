from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.contact import Contact
from model.group import Group
import re
__author__ = 'Sofia'


class ContactHelper():
    def __init__(self, app):
        self.app = app



    def create(self, new_contact_data):
        # create contact
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_data(new_contact_data)
        wd.find_element(By.XPATH, '//div[@id="content"]/form/input[20]').click()
        #self.check_main_page()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, 'input[id="%s"]' % contact_id).click()
        wd.find_element(By.XPATH, '//select[@name="to_group"]/option[contains(@value, "%s")]' % group_id).click()
        wd.find_element(By.XPATH, '//input[@value="Add to"]').click()

    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()

        wd.find_element(By.XPATH, '//select[@name="group"]/option[contains(@value, "%s")]' % group_id).click()
        wd.find_element(By.CSS_SELECTOR, 'input[id="%s"]' % contact_id).click()
        wd.find_element(By.XPATH, '//input[@name="remove"]').click()

    def username(self):
        wd = self.app.wd
        return "admin"

    def check_main_page(self):
        # return to main page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def del_first_contact(self):
        self.del_contact_by_index(0)
        self.contact_cache = None

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        #self.select_contact_by_index(index)
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, '//input[@value="Delete"]').click()
        # Принять предупреждение
        # Явное ожидание появления сообщения об успешном удалении
        try:
            WebDriverWait(wd, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.msgbox"))
            )
        except TimeoutException:
            print("Сообщение об успешном удалении не появилось за отведенное время.")
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[id='%s']" % id).click()
        wd.find_element(By.XPATH,"//input[@value='Delete']").click()
        self.cont_cache = None


    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # edit contact
        wd.find_elements(By.XPATH, '//img[@alt="Edit"]')[index].click() #+[index]
        self.fill_contact_data(new_contact_data)
        #submit contact update
        wd.find_element(By.NAME, 'update').click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_edit_by_id(id)
        self.fill_contact_data(contact)
        wd.find_element(By.NAME, 'update').click()
        self.app.open_home_page()
        self.cont_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, '//img[@alt="Edit"]')[index].click()

    def open_contact_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, '//a[contains(@href,"edit.php?id=%s")]' % id).click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        fax = wd.find_element(By.NAME, "fax").get_attribute("value")
        email = wd.find_element(By.NAME,"email").get_attribute("value")
        email2 = wd.find_element(By.NAME,"email2").get_attribute("value")
        email3 = wd.find_element(By.NAME,"email3").get_attribute("value")
        address = wd.find_element(By.NAME,"address").get_attribute("value")
        return Contact(firstname= firstname, lastname= lastname, id = id, homephone= homephone, workphone= workphone, mobilephone= mobilephone, fax= fax, email3= email3, email2= email2, email= email, address= address)



    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        print(text)
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)

        return Contact(homephone=homephone,  mobilephone=mobilephone, workphone=workphone,fax=fax)

    def fill_contact_data(self, contact):
        #wd = self.app.wd
        self.change_filed_value("firstname", contact.firstname)
        self.change_filed_value("lastname", contact.lastname)
        self.change_filed_value("company", contact.company)
        self.change_filed_value("address", contact.address)
        self.change_filed_value("mobile", contact.mobile)
        self.change_filed_value("nickname", contact.nickname)
        self.change_filed_value("title", contact.title)
        self.change_filed_value("home", contact.homephone)
        self.change_filed_value("work", contact.workphone)
        self.change_filed_value("mobile", contact.mobile)
        self.change_filed_value("fax", contact.fax)
        self.change_filed_value("email", contact.email)
        self.change_filed_value("email2", contact.email2)
        self.change_filed_value("email3", contact.email3)
        self.change_filed_value("homepage", contact.homepage)
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
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, address= address)) #, fax= all_phones[3]
        return list(self.contact_cache)


    def alert_accept(self):
        wd = self.app.wd
    # Принять предупреждение
        wd.switch_to.alert.accept()
    # Явное ожидание появления сообщения об успешном удалении
        try:
            WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.msgbox"))
            )
        except TimeoutException:
           print("Сообщение об успешном удалении не появилось за отведенное время.")

