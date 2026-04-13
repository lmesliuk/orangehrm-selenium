# OrangeHRM Login Test Automation Framework

A small QA automation project built with Python, Selenium, and pytest using the Page Object Model (POM).

This project automates two login scenarios for the OrangeHRM demo site and was created as a portfolio piece to demonstrate clean test design, reusable page objects, explicit waits, screenshots, logging, and HTML reporting.

## Project overview

The project covers two basic but important test cases:

- Successful login with valid credentials
- Unsuccessful login with invalid credentials

Even though the scope is intentionally small, the framework structure was designed to be clean, scalable, and aligned with common automation practices used in real QA projects.

## Tech stack

- Python
- Selenium WebDriver
- Pytest
- Webdriver Manager
- Pytest HTML Report

## Implemented practices

- Page Object Model (POM)
- BasePage for reusable common actions
- Pytest fixture for WebDriver setup and teardown
- Explicit waits
- UI and navigation assertions
- Screenshot capture
- Basic logging
- HTML test reporting

## Project structure

```text
orangehrm-selenium/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   └── test_login.py
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
└── README.md
```

## Test cases
- 1. Successful login

Validates that a user can log in with correct credentials and successfully reach the dashboard.

- 2. Invalid login

Validates that the correct error message is displayed when invalid credentials are submitted.

## Installation

Create and activate a virtual environment, then install dependencies:

```text
pip install -r requirements.txt
```

## Run tests
pytest -s -v

## Generate HTML report
```text
pytest -v --html=reports/report.html --self-contained-html
```

## Notes

```text
This project is intentionally small in scope and focused on demonstrating maintainable automation structure rather than broad functional coverage. It serves as a foundation that can later be expanded with additional pages, more test cases, reporting improvements, and CI integration.
```