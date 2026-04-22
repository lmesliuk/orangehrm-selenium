import pytest    
from pages.buzz_page import BuzzPage
from selenium.webdriver.common.by import By


def test_buzz_page_elements(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()

    assert buzz_page.is_buzz_header_displayed(), "Buzz header is not displayed"
    assert buzz_page.is_buzz_post_input_displayed(), "Buzz post input is not displayed"
    
def test_post_buzz_message(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()

    assert buzz_page.is_buzz_post_input_displayed(), "Buzz post input is not displayed"
    
    test_message = "Hello, this is a test message!"
    buzz_page.type(buzz_page.BUZZ_POST_INPUT, test_message)
    # Luego, podrías agregar una verificación para asegurarte de que el mensaje se publicó correctamente, como buscar el mensaje en la página o verificar que se muestra un mensaje de éxito.   
    assert buzz_page.get_text((By.XPATH, "//div[contains(@class, 'buzz-post') and contains(text(), '" + test_message + "')]")) == test_message, "Buzz message was not posted successfully"