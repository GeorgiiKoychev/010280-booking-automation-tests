from behave import when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@when('the user opens the filter menu')
def step_open_filters(context):
    filter_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Filter")'))
    )
    filter_button.click()

@when('the user selects the filter "{filter_name}"')
def step_select_filter(context, filter_name):
    max_swipes = 10
    found = False

    for i in range(max_swipes):
        try:
           
            text_element = context.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{filter_name}")'
            )

    
            checkbox = context.driver.find_element(
                AppiumBy.XPATH,
                f'//android.widget.TextView[contains(@text, "{filter_name}")]/following-sibling::android.widget.CheckBox'
            )
            if checkbox.get_attribute("checked") != "true":
                checkbox.click()

            found = True
            break  
        except:
            context.driver.swipe(500, 1600, 500, 600, 300)
            sleep(0.3)

    if not found:
        raise AssertionError(f"Could not find or select filter '{filter_name}' after scrolling.")

@when('the user applies the filters')
def step_apply_filters(context):
    apply_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show results")'))
    )
    apply_button.click()

@then('the results should match the selected filters')
def step_verify_filtered_results(context):
    sleep(2)
    hotel_cards = context.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
    assert len(hotel_cards) > 0, "No results displayed after applying filters"

    downtown_matches = [card for card in hotel_cards if "downtown" in card.get_attribute("content-desc").lower()]
    assert downtown_matches, "No filtered results mention 'downtown' or expected tags"
