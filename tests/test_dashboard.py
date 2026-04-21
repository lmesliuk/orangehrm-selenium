import logging
import os
from pages.dashboard_page import DashboardPage



def test_invalid_login(driver):
    login_page = LoginPage(driver)

    logger.info("Starting invalid login test")
    login_page.open()
    logger.info("Login page opened")

    login_page.login("Admin", "wrongpassword")
    logger.info("Invalid credentials submitted")

    error_message = login_page.get_error_message()
    logger.info(f"Error message displayed: {error_message}")

    assert error_message == "Invalid credentials"

    os.makedirs("screenshots", exist_ok=True)
    login_page.take_screenshot("screenshots/invalid_login.png")
    logger.info("Screenshot saved: screenshots/invalid_login.png")
