from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('the user taps on the "Flights" tab')
def step_tap_flights(context):
    flights_tab = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Flights")'))
    )
    flights_tab.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().descriptionContains("SOF Sofia Airport")'))
    )

@when('the user selects "Berlin" as the destination')
def step_select_flight_destination(context):
    to_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("flights_search_box_to_field")'))
    )
    to_field.click()

    input_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID,
        "com.booking:id/search_destination_query_input"))
    )
    input_box.send_keys("Berlin")

    #remove if clipboard pops up
    try:
        clipboard_bar = context.driver.find_element(
            AppiumBy.ID, "com.google.android.inputmethod.latin:id/clipboard_header")
        if clipboard_bar.is_displayed():
            context.driver.press_keycode(4)
            sleep(0.3)
    except:
        pass 

    result = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID,
        "com.booking:id/destination_item_name"))
    )
    result.click()

@when('the user selects departure and return dates')
def step_select_flight_dates(context):
    calendar_done_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID,
        "com.booking:id/flights_calendar_cta"))
    )
    calendar_done_button.click()

@when('the user confirms the flight search')
def step_confirm_flight_search(context):
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("FlightsSearchBoxCta")'))
    )
    search_button.click()

@then('the flight results should be displayed')
def step_verify_flight_results(context):
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("results")'))
    )
