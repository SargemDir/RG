from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    url = 'https://ramat-gan.muni.il'

    header_toshavim_button = (
        By.XPATH,
        "//li[1]/ul/li[1]//span[2]"
    )

    toshavim_sherutim_hirum_button = (
        By.CSS_SELECTOR,
        "li.item-container:nth-child(10) > a:nth-child(1)"
    )

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def click_toshavim_button(self):
        self.click(self.header_toshavim_button)

    def toshavim_sherutim_hirum_button_is_visible(self):
        return self.wait_visible(self.toshavim_sherutim_hirum_button)
