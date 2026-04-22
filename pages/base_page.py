from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BasePage class to be inherited by all page classes
class BasePage:    
    # Base URL for all pages    
    BASE_URL = "https://opensource-demo.orangehrmlive.com"

    # Methods for all pages
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def type(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.find_clickable(locator).click()

    def get_text(self, locator):
        return self.find_visible(locator).text

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

