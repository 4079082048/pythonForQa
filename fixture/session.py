from selenium.webdriver.common.by import By

__author_ = 'Sofia'

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        #  login
        wd = self.app.wd
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.NAME, "user").click()

