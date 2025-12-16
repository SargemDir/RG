from conftest import driver
from pages.base_page import BasePage

class MivzakimPage(BasePage):
    url = 'https://ramat-gan.muni.il/notifications'

    title = ("css selector", "h2[class~=heading] > .brand-color")


    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def is_title_visible(self):
        return self.wait_visible(self.title)

    def get_title(self):
        element = self.wait_visible(self.title)
        return element.text



