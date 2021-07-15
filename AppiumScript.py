import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "deviceName": "Test",
    "platformName": "Android",
    "platformVersion": "11",
    "app": "/Users/danilov.and/Documents/Python_Appium_uiAutomator2/app/1xBet_base.apk",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "useNewWDA": "false",
    "usePrebuiltWDA": "true"
}

driver = webdriver.Remote('http://127.0.0.1:5905/wd/hub', desired_capabilities=desired_capabilities)


driver.implicitly_wait(10)

time.sleep(5)

print("Жмяк")
driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
driver.find_element_by_id("logout_item_drawer").click()
time.sleep(3)
driver.find_element_by_id("button2")

time.sleep(10)
