from time import sleep

from tests.base_test import BaseTest

class TestHome(BaseTest):

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
    def test_mivzakim_opened(self):
        self.home_page.open_page()
        self.home_page.click_mivzakim_button()
        assert self.mivzakim_page.is_title_visible()
        assert self.mivzakim_page.get_title() == "מבזקים"

    # Header click on תושבים button, sherutim area, parking openning
    def test_toshavim_parking_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_hanaya()
        self.parking_page.parking_page_is_opened()
        self.parking_page.is_titleParking_exists()

    # Header click on תושבים button, sherutim area, arnona openning
    def test_toshavim_arnona_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_arnona()
        self.arnona_page.arnona_page_is_opened()
        self.arnona_page.is_titleArnona_exists()

    # Header click on תושבים button, sherutim area, shchuna openning
    def test_toshavim_shchuna_sheli_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_shchuna_sheli()
        self.myNeighborhood_page.myNeighborhood_page_is_opened()
        self.myNeighborhood_page.is_title_myNeighborhood_exists()


    # Header click on תושבים button, sherutim area, merkaz sheyrut openning
    def test_toshavim_serviceCenter_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_merkaz_sheyrut()
        self.service_center_page.serviceCenter_page_is_opened()
        self.service_center_page.is_title_serviceCenter_exists()

    # Header click on תושבים button, sherutim area, רווחה ובריאות, revaha openning
    def test_toshavim_revaha_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_revachaVeBriut()
        self.home_page.click_on_revaha()
        self.revaha_page.revaha_page_is_opened()
        self.revaha_page.is_title_revaha_page_exists()

    # Header click on תושבים button, sherutim area, רווחה ובריאות, briut openning
    def test_toshavim_briut_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_revachaVeBriut()
        self.home_page.click_on_briut()
        self.health_page.health_page_is_opened()
        self.health_page.is_title_health_page_exists()

    # Header click on תושבים button, sherutim area, sviva openning
    def test_toshavim_sviva_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_sviva()
        self.environment_page.environment_page_is_opened()
        self.environment_page.is_title_environment_page_exists()

    # Header click on תושבים button, sherutim area, baaleyHaim openning
    def test_toshavim_baaleyHaim_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_baaleyHaim()
        self.baaleyHaim_page.baaleyHaim_page_is_opened()
        self.baaleyHaim_page.is_title_baaleyHaim_page_exists()

    # Header click on תושבים button, sherutim area, sababus openning
    def test_toshavim_sababus_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_sababus()
        self.sababus_page.sababus_page_is_opened()
        self.sababus_page.is_title_sababus_page_exists()

    # Header click on תושבים button, sherutim area, andasa openning
    def test_toshavim_engineering_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_handasa()
        self.engineering_page.engineering_page_is_opened()
        self.engineering_page.is_title_engineering_page_exists()

    # Header click on תושבים button, sherutim area, hirum openning
    def test_toshavim_emergency_opened(self):
        self.home_page.open_page()
        self.home_page.click_toshavim_button()
        self.home_page.click_on_hirum()
        self.emergency_page.emergency_page_is_opened()
        self.emergency_page.is_title_emergency_page_exists()