import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver():
    options = Options()

    if os.getenv("CI") == "true" or sys.platform.startswith("linux"):
        # Docker / CI
        options.binary_location = "/usr/bin/chromium"
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=2560,1440")

        service = Service("/usr/bin/chromedriver")

    else:
        # Local (Windows / macOS)
        from webdriver_manager.chrome import ChromeDriverManager

        options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
