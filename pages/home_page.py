from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    url = 'https://ramat-gan.muni.il'
    toshavim_button = (By.XPATH, "//li[1]/ul/li[1]//span[2]")
    # TO DO header_toshavim_page
    toshavim_sherutim_hirum_button = (By.CSS_SELECTOR, "li.item-container:nth-child(10) > a:nth-child(1)")
    header_asakim_button = (By.XPATH, "//li[1]/ul/li[2]//span[2]")
    # TO DO header_asakim_page
    asakim_asakimBeDigital_gmarHeshbon_button = (By.XPATH,"//app-header/app-main-menu-expanded/div[2]/div/div[2]/ul/li[4]/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.header_mivzakim_button = None

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def click_toshavim_button(self):
        self.click(self.toshavim_button)

    def toshavim_sherutim_hirum_button_is_visible(self):
        return self.wait_visible(self.toshavim_sherutim_hirum_button)

    def click_asakim_button(self):
        self.click(self.header_asakim_button)

    def asakim_asakimBeDigital_gmarHeshbon_button_is_visible(self):
        return self.wait_visible(self.asakim_asakimBeDigital_gmarHeshbon_button)

    def click_mivzakim_button(self):
        self.click(self.header_mivzakim_button)
