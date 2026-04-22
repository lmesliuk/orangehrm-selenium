# 🧠 Selenium Common Errors — Cheat Sheet

## StaleElementReferenceException

### What it means
Selenium found an element, saved it, but by the time it tried to use it,
the page had redrawn that element. The saved reference is now "stale" (old/rancid).

### When it happens
- Pages built with React, Vue, or Angular (they redraw elements constantly)
- After typing in an input — the page updates internally
- After any action that triggers a page re-render

### Visualized
```
1. Selenium finds the button → saves its location
2. You type in the textarea
3. The page redraws internally 🔄
4. Selenium tries to click the saved location → element is gone → 💥 StaleElement
```

### Fix
Use `find_clickable` instead of `find_visible` for buttons you interact with.
`find_clickable` re-fetches the element fresh, right before clicking.

```python
# ❌ find_visible — finds once, saves, then clicks (can go stale)
def click_post_button(self):
    self.find_visible(self.BUZZ_POST_BUTTON).click()

# ✅ find_clickable — finds fresh right before clicking
def click_post_button(self):
    self.find_clickable(self.BUZZ_POST_BUTTON).click()
```

---

## TimeoutException

### What it means
Selenium waited (default 10 seconds) for an element to appear or be visible,
but it never showed up.

### When it happens
- The locator (XPATH, CSS) is wrong → element not found
- The page didn't load in time
- The user is not logged in → page redirected to login instead

### Visualized
```
Selenium: "I'll wait up to 10 seconds for this element..."
Page: 🦗🦗🦗
Selenium: "Time's up." → 💥 TimeoutException
```

### Fix checklist
1. Check the locator — inspect the element again, maybe the HTML changed
2. Check if login is required — is conftest.py logging in before the test?
3. Check if the page actually loaded — add a `wait_for_url_contains` before finding elements

```python
# Example: make sure you're on the right page before looking for elements
def open(self):
    self.driver.get(self.URL)
    self.wait_for_url_contains("buzz")  # ← confirms page loaded
```

---

## NoSuchElementException

### What it means
Selenium looked for an element and it simply doesn't exist in the DOM.

### Difference from TimeoutException
- `TimeoutException` → waited and waited, never appeared
- `NoSuchElementException` → didn't even wait, just looked once and it's not there

### Fix
Same as TimeoutException — check the locator first.

---

## ElementNotInteractableException

### What it means
Selenium found the element but can't interact with it —
it might be hidden, disabled, covered by another element, or off-screen.

### Fix
Use `find_clickable` instead of `find_visible` —
it waits until the element is both visible AND interactable.

---

## Quick reference

| Error | Likely cause | Fix |
|---|---|---|
| `StaleElementReferenceException` | Page redrawn after element was found | Use `find_clickable` |
| `TimeoutException` | Element never appeared | Check locator or login |
| `NoSuchElementException` | Element doesn't exist in DOM | Check locator |
| `ElementNotInteractableException` | Element exists but can't be clicked | Use `find_clickable` |

---

*Every error is a lesson. 🐛*