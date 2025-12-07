# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self, base_url):
        self.go_to(base_url)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error(self):
        return self.find(self.ERROR_MSG).text

    def is_logged_in(self):
        return "inventory" in self.driver.current_url

    def is_error_displayed(self):
        try:
            return self.find(self.ERROR_MSG).is_displayed()
        except:
            return False
