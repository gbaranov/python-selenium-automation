# Created by Georgy Baranov at 6/21/2020
Feature: Test Scenarios for Search functionality

  Scenario: User can search for order cancelation in Help section
    Given Open Amazon Help page
    When Input Cancel Orders into search field
    And Click on search icon
    Then Results for Cancel Orders are shown