from pages.base_page import BasePage

class InteractionFormPage(BasePage):
    url = 'https://ramat-gan.muni.il/interaction-form'

    # Pniyot elements, level 1
    aher= ("css selector", "#mat-mdc-checkbox-14  label")

    # elements, level 2
    street_name_field = ("css selector", "#streetName")
    accept_street_name = ("css selector", ".mdc-list-item__primary-text")
    number_building_field = ("css selector", "#houseNumber")
    report_field = ("css selector", "#report")

    emscheh_lvl1_button = ("css selector", ".rg-button > span:nth-child(2)")
    emscheh_lvl2_button = ("css selector", ".primary > span > span")
    emscheh_lvl3_button = ("css selector", ".primary > span > span")
    select_file_locator = ("css selector", ".select-file")





    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def check_aher_element_checkbox(self):
        self.wait_visible(self.aher)
        self.click(self.aher)

    def click_on_emshech_lvl1_button(self):
        self.click(self.emscheh_lvl1_button)

    def click_on_emshech_lvl2_button(self):
        self.click(self.emscheh_lvl2_button)

    def input_street(self):
        self.type(self.street_name_field, "דרך אבא הלל")
        self.wait_visible(self.accept_street_name)
        self.click(self.accept_street_name)

    def input_number_building(self):
        self.type(self.number_building_field, "14")

    def input_address(self):
        self.input_street()
        self.input_number_building()

    def fill_report_and_go_to_next_page(self):
        self.type(self.report_field, "בדיקה, נא למחוק")
        self.click_on_emshech_lvl2_button()

    def fill_data_and_go_to_next_page(self):
        self.input_address()
        self.fill_report_and_go_to_next_page()








