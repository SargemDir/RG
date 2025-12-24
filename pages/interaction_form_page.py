from pages.base_page import BasePage

class InteractionFormPage(BasePage):
    url = 'https://ramat-gan.muni.il/interaction-form'

    # Pniyot elements, level 1
    aher= ("css selector", "#mat-mdc-checkbox-14  label")

    # elements, level 2
    street_name_field = ("css selector", "")

    emscheh_button = ("css selector", ".rg-button > span:first-child")




    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(self.url)
        self.is_opened(self.url)

    def check_aher_element_checkbox(self):
        self.wait_visible(self.aher)
        self.click(self.aher)

    def click_on_emshech_button(self):
        self.wait_visible(self.emscheh_button)
        self.click(self.emscheh_button)




