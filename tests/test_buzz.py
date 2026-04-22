import time

import pytest    
from pages import buzz_page
from pages.buzz_page import BuzzPage
from selenium.webdriver.common.by import By

def test_buzz_page_elements(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()
    #assert buzz_page.is_buzz_header_displayed(), "Buzz header is not displayed"
    #assert buzz_page.is_buzz_post_input_displayed(), "Buzz post input is not displayed"
    
def test_post_buzz_message(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()
    test_message = "Surprise"
    buzz_page.post_message(test_message)
    buzz_page.click_post_button()
    time.sleep(2)
    buzz_page.refresh_page()  
    time.sleep(2)    
    assert test_message in buzz_page.get_latest_post_text(test_message), "Buzz message was not posted successfully"
