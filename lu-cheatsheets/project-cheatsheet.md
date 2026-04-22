
# 🧠 Project Reminders & Notes

## How conftest.py and fixtures work

The `conftest.py` file contains **fixtures** — setup code that runs automatically before each test.

Think of it as a sequence of steps:

```
conftest.py (runs first)       test file (runs after)
──────────────────────         ──────────────────────
1. Open browser           →
2. Open login page        →
3. Log in                 →
4.                        →    Navigate to the page you need
5.                        →    Do the test actions
6.                        →    Assert the expected result
```

### Why do it this way?

Without this, every test would need to repeat the login steps — that's duplicated code and harder to maintain.

With the fixture, the browser is always **ready and logged in** before each test starts. Each test only needs to worry about what it actually wants to test.

### Example

```python
# conftest.py — runs before EVERY test automatically
@pytest.fixture
def driver():
    driver = webdriver.Chrome(...)
    driver.maximize_window()

    # Login once, before handing the driver to the test
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123")

    yield driver      # ← here the test runs
    driver.quit()     # ← this runs after the test finishes


# test_buzz.py — already logged in when this runs
def test_post_buzz_message(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()       # just navigate, no need to login again
    ...
```

### The yield keyword

`yield` is the moment the fixture "pauses" and hands control to the test.
Everything **before** yield = setup. Everything **after** yield = teardown (cleanup).

```
setup   →   yield   →   test runs   →   teardown
open browser         →               →   driver.quit()
login                →               →
```

---

## Locator strategy

Locators are stored as **class-level tuples** using `By`:

```python
BUZZ_POST_INPUT = (By.XPATH, '//textarea[@placeholder="What\'s on your mind?"]')
```

For **dynamic locators** (where part of the locator changes), build them inside the method using f-strings:

```python
# Store the fixed part as a plain string (no tuple)
BUZZ_POST_BODY = "//div[contains(@class, 'orangehrm-buzz-post-body')]"

# Combine in the method with the dynamic part
def get_latest_post_text(self, message):
    locator = (By.XPATH, f"{self.BUZZ_POST_BODY}//p[contains(text(), '{message}')]")
    return self.find_visible(locator)
```

Why? Because class-level constants are fixed — they can't have variable parts.
Dynamic locators need to be built at runtime, inside a method.

---

*These are personal notes written while building this project. They reflect real mistakes and real learnings. 🐛*