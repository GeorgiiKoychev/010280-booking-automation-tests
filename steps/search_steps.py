from behave import given, when, then
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta

@given('the app is opened')
def step_impl(context):

    context.driver.implicitly_wait(10)
    sleep(1)

    try:
        cookies = context.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Accept")'
        )
        cookies.click()
    except NoSuchElementException:
        pass

    try:
        no_thanks = context.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Button").instance(3)'
        )
        no_thanks.click()
    except NoSuchElementException:
        pass

    try:
        context.driver.execute_script("mobile: shell", {
            'command': 'input',
            'args': ['keyevent', 'KEYCODE_BACK']
        })
        sleep(0.5)
    except:
        pass

    try:
        close_login = context.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Navigate up")')
        close_login.click()
    except NoSuchElementException:
        pass

@when('the user taps the search field')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Enter your destination")'))
    ).click()

@when('the user enters "Sofia" and selects the suggested result')
def step_impl(context):
    input_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
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
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("City in Bulgaria")')))
    suggestion.click()

@when('the user selects check-in and check-out dates')
def step_impl(context):
    today = datetime.today()
    checkin_date = today.strftime('%#d %B %Y')
    checkout_date = (today + timedelta(days=1)).strftime('%#d %B %Y')

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//android.view.View[contains(@content-desc, '{checkin_date}')]"))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//android.view.View[contains(@content-desc, '{checkout_date}')]"))
    ).click()

    confirm = context.driver.find_element(By.ID, "com.booking:id/facet_date_picker_confirm")
    confirm.click()

@when('the user selects 2 adults as guests')
def step_impl(context):
    guests_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionContains("room")'
        ))
    )
    guests_button.click()

    confirm = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.booking:id/group_config_apply_button"))
    )
    confirm.click()

@when('the user confirms the search')
def step_impl(context):
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Search")'
        ))
    )
    search_button.click()

@then('search results should be displayed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.booking:id/sr_fragment_container"))
    )

