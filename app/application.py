from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.saved_page import SavedPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.search_page = SearchPage(driver)
        self.saved_page = SavedPage(driver)
