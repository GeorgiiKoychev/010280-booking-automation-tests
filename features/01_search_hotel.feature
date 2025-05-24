Feature: Hotel search on Booking.com

  Scenario: User searches for hotel in Sofia for two adults
    Given the app is opened
    When the user taps the search field
    And the user enters "Sofia" and selects the suggested result
    And the user selects check-in and check-out dates
    And the user selects 2 adults as guests
    And the user confirms the search
    Then search results should be displayed 

    