from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author_ = 'Sofia'

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        #  login
        wd = self.app.wd
        self.app.open_home_page()
        #WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "user")))
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        # Ожидание появления элемента "Logout"
        #WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        wd.find_element(By.LINK_TEXT, "Logout").click()
        #WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "user")))
        wd.find_element(By.NAME, "user").click()

    def ensure_logout(self):
        wd =self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        #return len(wd.find_element(By.LINK_TEXT, "Logout")) > 0
        return len(wd.find_elements(By.XPATH, "/html/body/div/div[1]/form/a")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, "//div/div[1]=/form'/b").text == "(" + username + ")"
