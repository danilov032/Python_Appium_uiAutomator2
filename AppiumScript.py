import time

from appium import webdriver
from selenium.webdriver.common.by import By

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

driver = webdriver.Remote('http://127.0.0.1:5901/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(10)

driver.find_element_by_id("org.wikipedia:id/search_container").click()

edit_text = driver.find_element_by_id("org.wikipedia:id/search_src_text")
edit_text.clear()
edit_text.send_keys("Python")

text = driver.find_element_by_id("org.wikipedia:id/page_list_item_title").text

assert 'Python' in text, f'Отсутствует слова Python в {text}'

print("Все")
