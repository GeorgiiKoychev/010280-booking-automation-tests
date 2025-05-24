Feature: Sorting search results

  Scenario: User sorts results by distance from city center
    Given the app is opened
    When the user taps the search field
    And the user enters "Sofia" and selects the suggested result
    And the user selects check-in and check-out dates
    And the user selects 2 adults as guests
    And the user confirms the search
    And the user opens the sorting options
    And the user selects "Distance From Downtown"
    Then the results should be sorted by proximity to the center
