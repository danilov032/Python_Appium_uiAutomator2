import time

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchPage(Page):
    SEARCH_FIELD = (By.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULT = (By.ID, "org.wikipedia:id/page_list_item_title")
    SEARCH_NAVIGATE = (By.ID, "org.wikipedia:id/main_nav_tab_layout")
    SEARCH_ICON = (By.CLASS_NAME, "android.widget.ImageView")

    def input_search(self, search_phrase: str):
        self.input(search_phrase, *self.SEARCH_FIELD)

    def verify_search_result(self, search_phrase: str):
        result_text = self.find_element(*self.SEARCH_RESULT).text
        assert search_phrase in result_text, f'Отсутствует слова {search_phrase} в {result_text}'

    def go_to_save_page(self):
        bar = self.driver.find_element(*self.SEARCH_NAVIGATE)
        save_but = bar.find_elements(*self.SEARCH_ICON)
        save_but[1].click()
