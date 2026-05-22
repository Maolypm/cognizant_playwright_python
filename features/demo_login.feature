Feature: User Login
  As a user of the practice website
  I want to enter my credentials
  To access the successful login area

  Background:
    Given the user opens the login page

  Scenario: Positive LogIn test
    When the user types username "practice" into Username field
    And the user types password "SuperSecretPassword!" into Password field
    And pushes Submit button
    Then the new page should contain expected text "You logged into a secure area!"

  Scenario: Negative password test
    When the user types username "practice" into Username field
    And the user types password "incorrectPassword" into Password field
    And pushes Submit button
    Then the error message text should be "Your password is invalid!"