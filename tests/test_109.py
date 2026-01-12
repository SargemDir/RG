from time import sleep

from tests.base_test import BaseTest

class TestMoked(BaseTest):

    # פנייה למוקד
    def test_109(self):
        self.interaction_form_page.open_page()
        self.interaction_form_page.check_aher_element_checkbox()
        self.interaction_form_page.click_on_emshech_lvl1_button()
        self.interaction_form_page.fill_data_and_go_to_next_page()
        self.interaction_form_page.upload_file_via_ui()
        sleep(10)

