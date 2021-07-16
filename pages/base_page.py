class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        e = self.driver.find_elements(*locator)
        e.click()

    def input(self, text, *locator):
        e = self.driver.find_elements(*locator)
        e.clear()
        e.send_keys(text)