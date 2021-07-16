from appium import webdriver


def before_scenario(context, scenario):
    desired_capabilities = {
        "deviceName": "Test",
        "platformName": "Android",
        "platformVersion": "10",
        "app": "/Users/danilov.and/Documents/Python_Appium_uiAutomator2/app/Википедия_base.apk",
        "noReset": "true",
        "unicodeKeyboard": "true",
        "useNewWDA": "false",
        "usePrebuiltWDA": "true",
        "automationName": "UiAutomator2"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:5901/wd/hub', desired_capabilities=desired_capabilities)

    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()
