import os
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options

def before_scenario(context, scenario):
    capabilities_path = os.path.join("configs", "capabilities.json")
    with open(capabilities_path) as f:
        caps = json.load(f)

    options = UiAutomator2Options().load_capabilities(caps)

    context.driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        options=options
    )

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

