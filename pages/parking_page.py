from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ParkingPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-security-and-enforcement/content-pages/parking-lobby'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def parking_page_is_opened(self):
        self.is_opened(self.url)

    def is_titleParking_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "חניה ברמת-גן"