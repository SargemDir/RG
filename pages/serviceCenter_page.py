from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ServiceCenterPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-ceo/business-units/service-center'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def serviceCenter_page_is_opened(self):
        self.is_opened(self.url)

    def is_title_serviceCenter_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "מרכז השירות לתושב"