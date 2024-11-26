from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

from selenium import webdriver


__author__ = 'Sofia'


class Application:
    def __init__(self, browser, baseUrl): #(self)

        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        #аварийное прерывание кода


        self.current_url = None
        self.wd = webdriver.Firefox() #self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.open_home_page()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = baseUrl


    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("index.php") > 0):
            wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


