# 🧠 Page Object Model (POM) — Personal Reminder

## What is POM?

POM is a design pattern that separates **where things are** from **what you test**.

Each page of the app has its own Python class. That class knows:
- Where the elements are (locators)
- How to interact with them (methods)

The test file only knows:
- What scenario to run
- What to assert

---

## Project structure

```
pages/
├── base_page.py       ← shared methods for ALL pages
├── login_page.py      ← locators + methods for the Login page
├── buzz_page.py       ← locators + methods for the Buzz page
└── dashboard_page.py  ← locators + methods for the Dashboard page

tests/
├── test_login.py      ← tests for login scenarios
└── test_buzz.py       ← tests for buzz scenarios

conftest.py            ← shared fixtures (browser setup, login)
```

---

## BasePage — the parent class

Contains reusable methods that every page needs.
All page classes **inherit** from it.

```python
class BasePage:
    BASE_URL = "https://opensource-demo.orangehrmlive.com"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def get_text(self, locator):
        return self.find_visible(locator).text
    
    # ... etc
```

---

## Page class — inherits from BasePage

Each page class:
- Inherits BasePage with `(BasePage)` → gets all shared methods for free
- Defines its own locators as class-level constants
- Defines its own methods for interacting with that page

```python
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BuzzPage(BasePage):          # ← inherits BasePage

    # URL
    URL = BasePage.BASE_URL + "/web/index.php/buzz/viewBuzz"

    # Locators — fixed, defined at class level
    BUZZ_HEADER = (By.XPATH, "//h6[text()='Buzz']")
    BUZZ_POST_BUTTON = (By.XPATH, "//button[contains(text(), 'Post')]")
    
    # For dynamic locators, store only the fixed part
    BUZZ_POST_BODY = "//div[contains(@class, 'orangehrm-buzz-post-body')]"

    # Methods — what you can DO on this page
    def open(self):
        self.driver.get(self.URL)

    def post_message(self, message):
        self.find_visible(self.BUZZ_POST_INPUT).send_keys(message)

    def click_post_button(self):
        self.click(self.BUZZ_POST_BUTTON)

    # Dynamic locator built inside the method using f-string
    def get_latest_post_text(self, message):
        locator = (By.XPATH, f"{self.BUZZ_POST_BODY}//p[contains(text(), '{message}')]")
        return self.find_visible(locator)
```

---

## Test file — only tests, nothing else

The test file should NOT know about HTML, locators, or Selenium.
It only calls page methods and asserts results.

```python
def test_post_buzz_message(driver):
    # Arrange — set up the scenario
    buzz_page = BuzzPage(driver)
    buzz_page.open()
    test_message = "Hello, this is a test message!"

    # Act — do the action
    buzz_page.post_message(test_message)
    buzz_page.click_post_button()

    # Assert — verify the result
    assert buzz_page.get_latest_post_text(test_message) is not None
```

This pattern is called **AAA: Arrange, Act, Assert** — a clean way to structure any test.

---

## Inheritance — how it works visually

```
BasePage
│   find_visible()
│   find_clickable()
│   click()
│   get_text()
│   type()
│   take_screenshot()
│
├── LoginPage
│       open()
│       login(user, password)
│       get_error_message()
│
├── BuzzPage
│       open()
│       post_message(text)
│       click_post_button()
│       get_latest_post_text(message)
│
└── DashboardPage
        open()
        get_welcome_message()
        is_menu_displayed()
```

Each page **adds** its own methods on top of what BasePage already provides.

---

## Golden rules of POM

| Rule | Why |
|---|---|
| Locators live in the page class, never in the test | Easy to update when the UI changes |
| Tests only call methods, never find elements directly | Tests stay clean and readable |
| One page = one class | Easy to find and maintain |
| BasePage has only generic, reusable methods | No page-specific logic in BasePage |

---

*Built while learning. Every bug was a lesson. 🐛*
