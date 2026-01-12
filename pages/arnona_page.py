from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ArnonaPage(BasePage):
    url = 'https://www.ramat-gan.muni.il/department-money/content-pages/arnona-header'

    title_locator = (By.CSS_SELECTOR, ".brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def arnona_page_is_opened(self):
        self.is_opened(self.url)

    def is_titleArnona_exists(self):
        self.wait_visible(self.title_locator)
        text = self.get_text(self.title_locator)
        print(text)
        assert text == "ארנונה ברמת-גן"