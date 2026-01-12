from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EmergencyPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-security-and-enforcement/business-units/emergency-ramat-gan'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def emergency_page_is_opened(self):
        self.is_opened(self.url)

    def is_title_emergency_page_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "חירום ברמת גן"