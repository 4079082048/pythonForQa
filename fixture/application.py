from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
import time
from selenium import webdriver


__author__ = 'Sofia'


class Application:
    def __init__(self, browser = "firefox"): #(self)
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        else browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized Browser %s" % browser) #аварийное прерывание кода


        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.current_url = None
        self.wd = webdriver.Firefox() #self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.open_home_page()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("index.php") > 0):
            wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


