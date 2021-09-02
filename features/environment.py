from appium import webdriver
from app.application import Application
from const import Const


def before_scenario(context, scenario):
    desired_capabilities = {
        "deviceName": "Test",
        "platformName": "Android",
        "platformVersion": "10",
        "app": Const.APP_PATH_FILE,
        "noReset": "true",
        "unicodeKeyboard": "true",
        "useNewWDA": "false",
        "usePrebuiltWDA": "true",
        "automationName": "UiAutomator2"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:5901/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
