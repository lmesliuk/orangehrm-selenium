from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Elements locators
    PATH = "/web/index.php/dashboard/index"
    URL = BasePage.BASE_URL + PATH

    #LATERAL_MENU = (By.CLASS_NAME, "oxd-main-menu")
    LATERAL_MENU = (By.XPATH, "//nav[@class='oxd-navbar-nav']//a[contains(@href, '/dashboard/index')]")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    
    # Methods
    def open(self):
        self.driver.get(self.URL)

    def is_lateral_menu_displayed(self):
        return self.find_visible(self.LATERAL_MENU).is_displayed()

    def get_dashboard_header_text(self):
        return self.get_text(self.DASHBOARD_HEADER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
