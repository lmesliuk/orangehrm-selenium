# Lu's BDD Reminders

A simple cheat sheet with the main BDD concepts.

## Main ideas

- User story: what the user wants or needs.
- BDD: how the system should behave to meet that need.
- Gherkin: a simple language to describe that behavior.
- Behave: a Python framework that runs Gherkin scenarios.

## Gherkin words

- Feature: a functionality or business goal.
- Scenario: one specific example of behavior.
- Given: the starting context.
- When: the user performs an action.
- Then: the expected result.
- And: an extra step or detail.

### Easy way to remember

- Given = where the user is / the initial state
- When = what the user does
- Then = what should happen

## Example

User story:  
As a user, I want to log in so that I can access my account.

BDD idea:  
The system should allow a valid user to log in successfully.

Gherkin example:

Scenario: Successful login  
  Given the user is on the login page  
  When the user enters valid credentials  
  And clicks the login button  
  Then the user should see the dashboard


## Feature

- A feature describes a functionality or business capability.
- It groups related scenarios.

### Easy way to remember:

- Feature = what we want to validate

## Scenario

- A scenario is one specific example of system behavior.
- It describes a flow with conditions, actions, and expected results.

### Easy way to remember:

- Scenario = one test situation


## Environment

- `environment.py` is optional in Behave.
- It is used for setup and teardown tasks.
- Common examples:
  - open and close the browser
  - prepare test data
  - configure shared objects in `context`
- It usually contains hooks such as:
  - `before_all`
  - `before_scenario`
  - `after_scenario`
  - `after_all`

### Easy way to remember:

- steps = test actions
- `environment.py` = test preparation and cleanup

## Hooks

- Hooks are special functions used before or after tests.
- They are usually written in `environment.py`.
- Common hooks:
  - `before_scenario`
  - `after_scenario`

### Easy way to remember:

- Hooks run automatically around the test


## Context

- Context: a shared object provided by Behave.
- It stores data that can be used across steps in the same scenario.
- We can add attributes dynamically, such as `context.driver`, `context.login_page`, or `context.response`.
- These attributes do not exist by default. We create them when needed.

### Easy way to remember:

- `context` = a shared backpack between steps


## Steps

- Steps: Python functions that match Gherkin sentences.
- They connect the scenario text to the automation code.
- Common step keywords:
  - `@given`
  - `@when`
  - `@then`
- Each step usually receives `context`.

### Easy way to remember:

- Gherkin says it
- the step does it

#Probando rama nueva