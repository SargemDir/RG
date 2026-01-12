import os
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InteractionFormPage(BasePage):
    url = "https://ramat-gan.muni.il/interaction-form"

    # Используем относительный путь к файлу
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "test.jpg")
    file_path = os.path.abspath(file_path)  # превращаем в абсолютный путь внутри контейнера/локально

    # ===== locators =====
    aher = (By.CSS_SELECTOR, "#mat-mdc-checkbox-14 label")
    emscheh_lvl1_button = (By.CSS_SELECTOR, ".rg-button > span:nth-child(2)")
    street_name_field = (By.CSS_SELECTOR, "#streetName")
    accept_street_name = (By.CSS_SELECTOR, ".mdc-list-item__primary-text")
    number_building_field = (By.CSS_SELECTOR, "#houseNumber")
    report_field = (By.CSS_SELECTOR, "#report")
    emscheh_lvl2_button = (By.CSS_SELECTOR, ".primary > span > span")
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    uploaded_file_block = (By.CSS_SELECTOR, "#loadedFile_0 .uploaded")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)

    # ===== navigation =====
    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def check_aher_element_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.aher)).click()

    def click_on_emshech_lvl1_button(self):
        self.wait.until(EC.element_to_be_clickable(self.emscheh_lvl1_button)).click()

    # ===== form =====
    def input_street(self):
        self.wait.until(EC.visibility_of_element_located(self.street_name_field)).send_keys(
            "דרך אבא הלל"
        )
        self.wait.until(EC.element_to_be_clickable(self.accept_street_name)).click()

    def input_number_building(self):
        self.wait.until(EC.visibility_of_element_located(self.number_building_field)).send_keys("14")

    def fill_report_and_go_to_next_page(self):
        self.wait.until(EC.visibility_of_element_located(self.report_field)).send_keys("בדיקה, נא למחוק")
        self.wait.until(EC.element_to_be_clickable(self.emscheh_lvl2_button)).click()

    def fill_data_and_go_to_next_page(self):
        self.input_street()
        self.input_number_building()
        self.fill_report_and_go_to_next_page()

    # ===== upload =====
    def upload_file_via_ui(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(self.file_path)

        file_input = self.find(self.file_input_locator)
        self.driver.execute_script(
            "arguments[0].style.display='block'; arguments[0].style.opacity=1;",
            file_input
        )
        file_input.send_keys(self.file_path)
