from datetime import datetime, timedelta
from behave import when
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@when('the user taps on "Car rental"')
def step_open_car_rental(context):
    car_rental_tab = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Car rental")'))
    )
    car_rental_tab.click()
    sleep(1)

@when('the user enters "Sofia" as pickup location and selects the suggested option')
def step_enter_pickup_location(context):
    pickup_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Enter a pick-up location")'))
    )
    pickup_field.click()

    input_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
    )
    input_field.send_keys("Sofia")
    
    #remove if clipboard pops up
    try:
        clipboard_bar = context.driver.find_element(
            AppiumBy.ID, "com.google.android.inputmethod.latin:id/clipboard_header")
        if clipboard_bar.is_displayed():
            context.driver.press_keycode(4)
            sleep(0.3)
    except:
        pass 

    suggestion = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sofia Airport")'))
    )
    suggestion.click()

@when('the user selects pickup and drop-off dates')
def step_select_car_dates(context):
    date_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Pick-up May")'))
    )
    date_field.click()

    # (here it is assumed that there are already dates selected)
    select_dates = WebDriverWait(context.driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Select dates").instance(1)'))
)
    select_dates.click()

@when('the user selects the pickup and drop-off times')
def step_select_car_times(context):
    select_times = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Select times").instance(1)'))
    )
    select_times.click()

@when('the user confirms the car rental search')
def step_confirm_car_search(context):
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Search")'))
    )
    search_button.click()

@then('the car rental results should be displayed')
def step_verify_car_results(context):
    sleep(2)
    results = context.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("results")')
    assert results, "No car rental results found on screen."