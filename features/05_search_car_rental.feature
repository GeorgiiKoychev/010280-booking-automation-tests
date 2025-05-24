Feature: Car rental search

  Scenario: User searches for a rental car in Sofia
    Given the app is opened
    When the user taps on "Car rental"
    And the user enters "Sofia" as pickup location and selects the suggested option
    And the user selects pickup and drop-off dates
    And the user selects the pickup and drop-off times
    And the user confirms the car rental search
    Then the car rental results should be displayed