from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RevahaPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-social-services/content-pages/welfare'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def revaha_page_is_opened(self):
        self.is_opened(self.url)

    def is_title_revaha_page_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "רווחה ברמת-גן"