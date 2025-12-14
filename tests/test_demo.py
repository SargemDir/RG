from tests.base_test import BaseTest

class TestDemo(BaseTest):

    # Header click on תושבים button and verify it's opened
    def test_toshavim_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        assert self.home_page.hirum_button_is_visible()

    # Header click on עסקים button and verify it's opened
    def test_asakim_opened(self):
        self.home_page.open_page()
        self.home_page.click_asakim_button()
        assert self.home_page.gmar_heshbon_button_is_visible()

    # Header click on מבזקים button and verify it's opened
    # def test_mivzakim_opened(self):
    #     self.home_page.open_page()
    #     self.home_page.click_mivzakim_button()
    #     assert self.home_page.title_is_visible()
