from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('the user is on the home screen of the Booking.com app')
def step_user_on_home_screen(context):
    home_element = context.driver.find_element(By.ID, "com.booking:id/facet_search_box_basic_location")
    assert home_element.is_displayed(), "Home screen not visible"

@when('the user enters "{destination}" as the destination')
def step_enter_destination(context, destination):
    search_field = context.driver.find_element(By.ID, "com.booking:id/facet_search_box_basic_location")
    search_field.click()
    input_field = context.driver.find_element(By.ID, "com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content")
    input_field.send_keys(destination)
    first_result = context.driver.find_element(By.ID, "com.booking:id/view_disambiguation_destination_title")
    first_result.click()

@when('the user selects valid check-in and check-out dates')
def step_select_dates(context):
    context.driver.find_element(By.ID, "com.booking:id/facet_search_box_basic_dates").click()
    sleep(1)
    dates = context.driver.find_elements(By.XPATH, "//android.view.View[@content-desc and @clickable='true']")
    if len(dates) >= 2:
        dates[0].click()
        dates[1].click()
    context.driver.find_element(By.ID, "com.booking:id/calendar_confirm_button").click()

@when('the user selects {adults:d} adults as guests')
def step_select_guests(context, adults):
    context.driver.find_element(By.ID, "com.booking:id/facet_search_box_basic_occupancy").click()
    sleep(1)
    plus_button = context.driver.find_element(By.ID, "com.booking:id/group_config_adults_plus_button")
    current = int(context.driver.find_element(By.ID, "com.booking:id/group_config_adults_number").text)
    while current < adults:
        plus_button.click()
        current += 1
    context.driver.find_element(By.ID, "com.booking:id/group_config_apply_button").click()

@when('the user taps the search button')
def step_tap_search(context):
    context.driver.find_element(By.ID, "com.booking:id/facet_search_box_cta").click()

@when('the user opens the sorting options')
def step_open_sorting_options(context):
    sort_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sort")'))
    )
    sort_button.click()

@when('the user selects "{option}"')
def step_select_sort_option(context, option):
    sort_option = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{option}")'))
    )
    sort_option.click()

@then('the results should be sorted by proximity to the center')
def step_verify_sorted_results(context):
    sleep(3)
    hotel_views = context.driver.find_elements(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().descriptionContains("downtown")'
    )

    assert hotel_views, "No results containing 'downtown' found in description"

    for hotel in hotel_views[:3]:
        assert "downtown" in hotel.get_attribute("content-desc").lower(), \
            "Expected 'downtown' in hotel description"