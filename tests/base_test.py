import pytest
from pages.home_page import HomePage
from pages.mivzakim_page import MivzakimPage

class BaseTest:

    home_page: HomePage
    mivzakim_page: MivzakimPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.mivzakim_page = MivzakimPage(driver)
