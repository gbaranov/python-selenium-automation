# Created by admin at 7/4/20
Feature: Amazon Cart validation

  Scenario: Validate and count amount of items in cart
    Given Open Amazon page
    When Input bag into search field
    And Click on item title
    And Click add to cart
    And Input hat into search field
    And Click on item title
    And Click add to cart
    And Click Cart
    Then Item is shown
