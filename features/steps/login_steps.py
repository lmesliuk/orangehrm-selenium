from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage


@given('the user is on the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)  
    context.login_page.open()


@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.login(username, password)


@then('the user should see the dashboard')
def step_see_dashboard(context):
    assert context.login_page.is_dashboard_displayed()


@then('the user should see the error message "{expected_message}"')
def step_see_error_message(context, expected_message):
    actual_message = context.login_page.get_error_message()
    assert expected_message in actual_message