from selenium.webdriver.common.by import By

from pages.base_page import Page


class SavedPage(Page):
    EMPTY_MESSAGE = (By.ID, "empty_message")

    def check_empty_page(self):
        # if self.driver.find_element(*self.EMPTY_MESSAGE)
# Дописать проверку есть ли элемент