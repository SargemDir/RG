from tests.base_test import BaseTest

class TestDemo(BaseTest):

    def test_toshavim_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        assert self.home_page.toshavim_sherutim_hirum_button_is_visible()
