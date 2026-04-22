
## XPATH quick reference

| Goal | XPATH example |
|---|---|
| Find by exact text | `//h6[text()='Buzz']` |
| Find by partial text | `//p[contains(text(), 'Hello')]` |
| Find by attribute | `//textarea[@placeholder="What's on your mind?"]` |
| Find by class | `//div[contains(@class, 'my-class')]` |
| Find child inside parent | `//div[@class='parent']//p` |
