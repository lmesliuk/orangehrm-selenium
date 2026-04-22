from email import message

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuzzPage(BasePage):
    
    # Elements locators
    PATH = "/web/index.php/buzz/viewBuzz"
    URL = BasePage.BASE_URL + PATH
    
    BUZZ_HEADER = (By.XPATH, "//h6[text()='Buzz']")
    BUZZ_POST_INPUT = (By.XPATH, '//textarea[@placeholder="What\'s on your mind?"]')
    BUZZ_POST_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'oxd-button--main')]")
    LATEST_POST_MESSAGE = (By.XPATH, "//div[contains(@class, 'orangehrm-buzz-post-body')]")
    BUZZ_POST_BODY = "//p[contains(@class, 'orangehrm-buzz-post-body-text')]"

    # Methods
    def open(self):
        self.driver.get(self.URL)
    
    def post_message(self, message):
        self.find_visible(self.BUZZ_POST_INPUT).send_keys(message)
    
    '''
    #No funciona porque se redibuja la página dinámicamente   
    def click_post_button(self):
        self.find_clickable(self.BUZZ_POST_BUTTON).click()
'''
    def click_post_button(self):
        button = self.find_clickable(self.BUZZ_POST_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
    '''
    # An option to combine the two steps into one method for convenience
    def post_message_complete(self, message):
        self.post_message(message)
        self.click_post_button()
    '''

    def is_buzz_header_displayed(self):
        return self.find_visible(self.BUZZ_HEADER) is not None 
    
    def is_buzz_post_input_displayed(self):
        return self.find_visible(self.BUZZ_POST_INPUT) is not None
    
    # Method to see post message
   # def get_latest_post_text(self, message):
   #     locator = (By.XPATH, f"{self.BUZZ_POST_BODY}[contains(text(), '{message}')]")
   #     return self.find_visible(locator).text 
    
    def refresh_page(self):
        self.driver.refresh()
    '''   
    def get_latest_post_text(self, message):
        locator = (By.XPATH, f"//p[contains(@class, 'orangehrm-buzz-post-body-text') and contains(text(), '{message}')]")
        text = self.find_visible(locator).text
        print(f">>> Texto encontrado: '{text}'")
        print(f">>> Locator: {locator}")
        return text
    '''
    def get_latest_post_text(self, message):
        locator = (By.XPATH, f"//p[contains(@class, 'orangehrm-buzz-post-body-text') and normalize-space()='{message}']")
        return self.find_visible(locator).text