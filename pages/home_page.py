from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    url = 'https://www.ramat-gan.muni.il'

    # Header buttons
    toshavim = (By.XPATH, "//header/div/nav/ul/li[1]/ul/li[1]")
    asakim = (By.XPATH, "//li[1]/ul/li[2]//span[2]")
    mivzakim = (By.CSS_SELECTOR, "header > div > [class^=flash]")
    peulot_ba_digital = ()
    pniya_le_moked = (By.CSS_SELECTOR, ".second-menu-part  app-menu-item> a > button > span:nth-child(2)")
    language_change = ()
    search = ()

    # Toshavim droped down buttons (when click on toshavim button)
        # שירותים
    hanaya_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='חניה']")
    arnona_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='ארנונה']")
    aShchunaSheli_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='השכונה שלי']")
    merkazSherut_locator = (By.XPATH, "//app-main-menu-expanded//div[1]/ul/li[4]/a")
    revachaVeBriut_locator = (By.XPATH, "//app-main-menu-expanded//li[5]/button/span")
    revaha_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='רווחה']")
    briut_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='בריאות']")
    sviva_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='סביבה']")
    baaleyHaim_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='בעלי חיים']")
    sababus_locator = (By.XPATH, "//app-main-menu-expanded//a[normalize-space()='סבבוס']")
    handasa_locator = (By.XPATH, "//div[@aria-labelledby='category-0']//a[normalize-space()='הנדסה']")
    hirum = (By.XPATH, "//div[@aria-labelledby='category-0']//a[normalize-space()='חירום']")
        # תרבות ופנאי
    events_locator = (By.XPATH, "//div[@aria-labelledby='category-1']//a[normalize-space()='אירועים']")
    tarbut_ve_omanut_locator = (By.XPATH, "//app-main-menu-expanded//li[2]/button/span")
    museums_locator = (By.XPATH, "//div[@aria-labelledby='category-1']//a[normalize-space()='מוזיאונים']")
    theaters_locator = (By.XPATH, "//div[@aria-labelledby='category-1']//a[normalize-space()='תיאטראות']")
    music_locator = (By.XPATH, "//a[@class='menu-link ng-tns-c2527924329-1'][normalize-space()='מוזיקה']")
    reshet_sifriyot_locator = (By.XPATH, "//app-main-menu-expanded//div[2]/ul/li[3]/a")


    # Asakim droped down buttons (when click on asakim button)
        # עסקים בדיגיטל
    gmar_heshbon = (By.XPATH, "//app-header/app-main-menu-expanded/div[2]/div/div[2]/ul/li[4]/a")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def click_toshavim_button(self):
        self.click(self.toshavim)

    def click_pniya_le_moked_button(self):
        self.click(self.pniya_le_moked)

    def hirum_button_is_visible(self):
        return self.wait_visible(self.hirum)

    def click_asakim_button(self):
        self.click(self.asakim)

    def gmar_heshbon_button_is_visible(self):
        return self.wait_visible(self.gmar_heshbon)

    def click_mivzakim_button(self):
        self.click(self.mivzakim)

    def click_on_hanaya(self):
        self.click(self.hanaya_locator)

    def click_on_arnona(self):
        self.click(self.arnona_locator)

    def click_on_shchuna_sheli(self):
        self.click(self.aShchunaSheli_locator)

    def click_on_merkaz_sheyrut(self):
        self.click(self.merkazSherut_locator)

    def click_on_revachaVeBriut(self):
        self.click(self.revachaVeBriut_locator)

    def click_on_revaha(self):
        self.click(self.revaha_locator)

    def click_on_briut(self):
        self.click(self.briut_locator)

    def click_on_sviva(self):
        self.click(self.sviva_locator)

    def click_on_baaleyHaim(self):
        self.click(self.baaleyHaim_locator)

    def click_on_sababus(self):
        self.click(self.sababus_locator)

    def click_on_handasa(self):
        self.click(self.handasa_locator)

    def click_on_hirum(self):
        self.click(self.hirum)