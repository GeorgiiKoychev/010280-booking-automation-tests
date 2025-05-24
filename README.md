Automated end-to-end tests for Android mobile app using Appium, Python, and Behave (BDD).
This project demonstrates how to automate UI scenarios such as searching for hotels, flights, and rental cars, including filtering and sorting results.
It also integrates with GitHub Actions for continuous integration and test validation.

Features
  Search for hotels with dynamic date selection
  Search for flights
  Search for rental cars
  Filter search results by review score
  Sort results by distance from city center
  Screenshot capture on test failure
  CI integration with GitHub Actions

Tools & Technologies
  Appium – cross-platform mobile automation framework
  Python – scripting and test logic
  Behave – BDD test framework using Gherkin syntax
  Android Studio – emulator and APK management
  Appium Inspector – locator analysis
  GitHub & GitHub Actions – version control and CI/CD

Project Structure
  booking_automation/
  ├── features/
  │   ├── 01_search_hotel.feature
  │   ├── 02_filter_by_rating.feature
  │   ├── 03_sort_by_distance.feature
  │   ├── 04_search_flight.feature
  │   └── 05_search_car_rental.feature
  ├── steps/
  │   ├── search_steps.py
  │   ├── filter_steps.py
  │   ├── sort_steps.py
  │   ├── flight_steps.py
  │   └── cars_steps.py
  ├── screenshots/
  ├── logs/
  ├── .github/
  │   └── workflows/
  │       └── python-app.yml
  └── README.md

Running the Tests:
  1.Start Appium server:
    
      appium --base-path /wd/hub
      
  2.Launch Android Emulator (Android Studio)
  
  3.Run tests:
  
        behave features/

This project uses GitHub Actions to trigger tests automatically on push.
On failure, screenshots are saved to the /screenshots folder. 
