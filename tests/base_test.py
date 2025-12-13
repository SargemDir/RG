import pytest
from pages.home_page import HomePage

class BaseTest:

    home_page: HomePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
