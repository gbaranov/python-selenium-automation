# Created by admin at 7/5/20
Feature: Best sellers page link validation

  Scenario: Validate 5 links at BestSellers
    Given Open Amazon page
    When Click Best Sellers link
    Then Verify links existence