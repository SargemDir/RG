import pytest
from pages.home_page import HomePage
from pages.mivzakim_page import MivzakimPage
from pages.interaction_form_page import InteractionFormPage
from pages.parking_page import ParkingPage
from pages.arnona_page import ArnonaPage
from pages.myNeighborhood_page import MyNeighborhoodPage
from pages.serviceCenter_page import ServiceCenterPage
from pages.revaha_page import RevahaPage
from pages.health_page import HealthPage
from pages.environment_page import EnvironmentPage
from pages.baaleyHaim_page import BaaleyHaimPage
from pages.sababus_page import SababusPage
from pages.engineering_page import EngineeringPage
from pages.emergency_page import EmergencyPage
class BaseTest:

    home_page: HomePage
    mivzakim_page: MivzakimPage
    interaction_form_page: InteractionFormPage
    parking_page: ParkingPage
    arnona_page: ArnonaPage
    myNeighborhood_page: MyNeighborhoodPage
    service_center_page: ServiceCenterPage
    revaha_page: 'RevahaPage'
    health_page: 'HealthPage'
    environment_page: 'EnvironmentPage'
    baaleyHaim_page: 'BaaleyHaimPage'
    sababus_page: 'SababusPage'
    engineering_page: 'EngineeringPage'
    emergency_page: 'EmergencyPage'

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.mivzakim_page = MivzakimPage(driver)
        request.cls.interaction_form_page = InteractionFormPage(driver)
        request.cls.parking_page = ParkingPage(driver)
        request.cls.arnona_page = ArnonaPage(driver)
        request.cls.myNeighborhood_page = MyNeighborhoodPage(driver)
        request.cls.service_center_page = ServiceCenterPage(driver)
        request.cls.revaha_page = RevahaPage(driver)
        request.cls.health_page = HealthPage(driver)
        request.cls.environment_page = EnvironmentPage(driver)
        request.cls.baaleyHaim_page = BaaleyHaimPage(driver)
        request.cls.sababus_page = SababusPage(driver)
        request.cls.engineering_page = EngineeringPage(driver)
        request.cls.emergency_page = EmergencyPage(driver)