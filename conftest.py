from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def browser():

    options = Options()

    options.add_argument("--headless=new")      # запуск без окна
    options.add_argument("--no-sandbox")        # обязательно для Docker
    options.add_argument("--disable-dev-shm-usage")  # обязательно для Docker
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver

    driver.quit()