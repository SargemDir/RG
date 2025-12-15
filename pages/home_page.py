from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    url = 'https://ramat-gan.muni.il'

    # Header buttons
    toshavim = ("xpath", "//header/div/nav/ul/li[1]/ul/li[1]")
    asakim = ("xpath", "//li[1]/ul/li[2]//span[2]")
    mivzakim = ()
    peulot_ba_digital = ()
    pniya_le_moked = ()
    language_change = ()
    search = ()

    # Toshavim droped down buttons (when click on toshavim button)
        # שירותים
    hirum = ("xpath", "//app-main-menu-expanded/div[2]/div/div[1]/ul/li[10]/a")

    # Asakim droped down buttons (when click on asakim button)
        # עסקים בדיגיטל
    gmar_heshbon = ("xpath", "//app-header/app-main-menu-expanded/div[2]/div/div[2]/ul/li[4]/a")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def click_toshavim_button(self):
        self.click(self.toshavim)

    def hirum_button_is_visible(self):
        return self.wait_visible(self.hirum)

    def click_asakim_button(self):
        self.click(self.asakim)

    def gmar_heshbon_button_is_visible(self):
        return self.wait_visible(self.gmar_heshbon)

    def click_mivzakim_button(self):
        self.click(self.mivzakim)
