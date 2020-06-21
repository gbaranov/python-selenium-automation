# Created by Georgy Baranov at 6/21/2020
Feature: Test Scenarios for Cart check

  Scenario: User can verify that cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify Cart is Empty