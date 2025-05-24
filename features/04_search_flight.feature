Feature: Searching for flights in Booking.com mobile app

  Scenario: User searches for a flight from Sofia to Berlin
    Given the app is opened
    When the user taps on the "Flights" tab
    And the user selects "Berlin" as the destination
    And the user selects departure and return dates
    And the user confirms the flight search
    Then the flight results should be displayed
