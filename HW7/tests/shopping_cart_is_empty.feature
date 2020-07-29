# Created by admin at 7/26/20
Feature: 'Your Shopping Cart is empty' shown if no product added

Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Shopping Cart is empty text present

  #Assignment description did require to check for Your Amazon Cart is empty