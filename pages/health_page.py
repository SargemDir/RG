from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HealthPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-social-services/business-units/health-care'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def health_page_is_opened(self):
        self.is_opened(self.url)

    def is_title_health_page_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "בריאות"