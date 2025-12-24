import pytest
from pages.home_page import HomePage
from pages.mivzakim_page import MivzakimPage
from pages.interaction_form_page import InteractionFormPage

class BaseTest:

    home_page: HomePage
    mivzakim_page: MivzakimPage
    interaction_form_page: InteractionFormPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.mivzakim_page = MivzakimPage(driver)
        request.cls.interaction_form_page = InteractionFormPage(driver)
