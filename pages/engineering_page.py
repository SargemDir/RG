from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EngineeringPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-engineering'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def engineering_page_is_opened(self):
        self.is_opened(self.url)

    def is_title_engineering_page_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "אגף הנדסה"