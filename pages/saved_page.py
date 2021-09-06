from selenium.webdriver.common.by import By

from pages.base_page import Page


class SavedPage(Page):
    EMPTY_MESSAGE = (By.ID, "empty_message")

    def check_empty_page(self):
        el = self.driver.find_element(*self.EMPTY_MESSAGE)
        assert el is not None, "Элемент отсутвует"
