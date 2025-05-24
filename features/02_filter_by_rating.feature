Feature: Filtering search results by rating

  Scenario: User filters results by review score
    Given the app is opened
    When the user taps the search field
    And the user enters "Sofia" and selects the suggested result
    And the user selects check-in and check-out dates
    And the user selects 2 adults as guests
    And the user confirms the search
    And the user opens the filter menu
    And the user selects the filter "Very Good: 8+"
    And the user applies the filters
    Then the results should match the selected filters