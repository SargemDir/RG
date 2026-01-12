import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

@pytest.fixture(scope="module")
def driver():
    options = Options()

    if sys.platform.startswith("linux"):
        # For CI / Ubuntu
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=2560,1440")
        service = Service(ChromeDriverManager().install())
    else:
        # For Windows local
        options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()