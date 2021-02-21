Feature: Test Plan For ParentLand

  Scenario: User successfully logged in
    Given User opens ParentLand
    Then It should have main logo visible
    Given User is logged in
    Then User logs out

  Scenario: User successfully sign up
    Given User opens ParentLand
    Then User accepts cookies
    Then User opens sign up page
    Then User sign up
    Then User can see success message

