import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    # Login before each test
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123") 
    yield driver
    driver.quit()
