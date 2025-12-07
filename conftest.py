# conftest.py
import pytest
import datetime
import os
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pytest_html import extras as pytest_html_extras
import requests

LOG_DIR = "reports/logs"
SCREENSHOT_DIR = "reports/screenshots"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def pytest_configure(config):
    # configurar logger básico para pytest
    logging.basicConfig(
        filename=f"{LOG_DIR}/execution_{datetime.datetime.now():%Y%m%d_%H%M%S}.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

@pytest.fixture(scope="session")
def base_url():
    # Cambia al site de pruebas que uses
    return "https://www.saucedemo.com"

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # quita si querés ver el navegador
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=chrome_options)
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook para tomar screenshot al fallar
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            filename = f"{SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
            try:
                driver_fixture.save_screenshot(filename)
                # adjuntar a pytest-html si está instalado
                if hasattr(item.config, "_html"):  
                    extra = getattr(rep, "extra", [])
                    extra.append(pytest_html.extras.png(filename))
                    rep.extra = extra
            except Exception as e:
                logging.exception("No se pudo guardar screenshot: %s", e)
