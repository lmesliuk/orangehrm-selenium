Feature: Login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters username "Admin" and password "admin123"
    Then the user should see the dashboard

  Scenario: Failed login with invalid credentials
    Given the user is on the login page
    When the user enters username "Admin" and password "wrongpass"
    Then the user should see the error message "Invalid credentials"