# Created by admin at 7/4/20
Feature: Amazon Cart validation

  Scenario: Validate and count amount of items in cart
    Given Open Amazon page
    When Input echo into search field
    And Click on item title
    And 