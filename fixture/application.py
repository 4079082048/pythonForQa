from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

__author__ = 'Sofia'



class Application:
    def __init__(self):
        self.current_url = None
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.open_home_page()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

  #  def open_home_page(self):
  #      wd = self.wd
  #      wd.get("http://localhost/addressbook/index.php")

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
