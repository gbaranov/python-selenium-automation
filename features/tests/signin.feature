# Created by admin at 6/14/20
Feature: Test scenario for Amazon Sign in

  Scenario: Logged out users sees sign in page when clicking Orders
    Given Open Amazon page
    When Click orders
    Then Verify Sign in page opened