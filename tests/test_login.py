import logging
import os

from pages.login_page import LoginPage


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def test_successful_login(driver):
    login_page = LoginPage(driver)

    logger.info("Starting successful login test")
    login_page.open()
    logger.info("Login page opened")

    login_page.login("Admin", "admin123")
    logger.info("Valid credentials submitted")

    assert login_page.wait_for_url_contains("/dashboard")
    assert login_page.is_dashboard_displayed()

    os.makedirs("screenshots", exist_ok=True)
    login_page.take_screenshot("screenshots/successful_login.png")
    logger.info("Screenshot saved: screenshots/successful_login.png")


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
