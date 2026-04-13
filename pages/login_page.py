from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_dashboard_displayed(self):
        return self.find_visible(self.DASHBOARD_HEADER).is_displayed()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
