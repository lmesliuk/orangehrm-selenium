from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuzzPage(BasePage):
    # Elements locators
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"
    BUZZ_HEADER = (By.XPATH, "//h6[text()='Buzz']")
    BUZZ_POST_INPUT = (By.XPATH, "//textarea[@placeholder='What's on your mind?']")

    # Methods
    def open(self):
        self.driver.get(self.URL)
        
    def is_buzz_header_displayed(self):
        return self.find_visible((By.XPATH, self.BUZZ_HEADER)) is not None 
    
    def is_buzz_post_input_displayed(self):
        return self.find_visible((By.XPATH, self.BUZZ_POST_INPUT)) is not None     
    
    # Method to see post message
    def get_buzz_post_message(self, message):
        locator = (By.XPATH, f"//div[contains(@class, 'buzz-post') and contains(text(), '{message}')]")
        return self.find_visible(locator).text