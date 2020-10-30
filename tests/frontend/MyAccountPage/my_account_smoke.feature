Feature: My Account Smoke Tests

  Scenario: Valid user should be able to login
    Given I go to the 'my account page
    When I 'bolofbaba@gmail.com into username of login form
    And I type 'bolofbaba' into password of login form
    And I click on the 'login' button
    Then user should be logged in
