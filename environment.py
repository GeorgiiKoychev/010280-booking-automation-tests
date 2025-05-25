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

def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = f"screenshot_{step.name}.png".replace(" ", "_").replace("/", "_")
        screenshot_path = os.path.join("screenshots", screenshot_name)

        try:
            context.driver.save_screenshot(screenshot_path)
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=step.name,
                    attachment_type=AttachmentType.PNG
                )
        except Exception as e:
            print(f"Неуспешно заснемане на screenshot: {e}")

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()

