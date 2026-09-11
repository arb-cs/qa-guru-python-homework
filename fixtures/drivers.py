from typing import Any, Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
@allure.title("Instantiate a driver for tests.")
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
@allure.title("Create an instance of the driver to which the window size can be passed.")
def desktop_driver(request) -> Generator[WebDriver, Any, None]:
    width, height = request.param

    if width < 1280:
        pytest.skip("The screen size is not valid for the desktop version of the website.")

    driver = webdriver.Chrome()
    driver.set_window_size(width, height)

    yield driver

    driver.quit()


@pytest.fixture()
@allure.title("Create an instance of a driver for tests that check the website’s responsiveness.")
def mobile_driver():
    driver = None

    def _create_driver(width, height):
        nonlocal driver
        if driver is not None:
            return driver

        mobile_emulation = {
            "deviceMetrics": {
                "width": width,
                "height": height,
                "pixelRatio": 3.0,
                "mobile": True,
                "touch": True
            },
            "userAgent": (
                "Mozilla/5.0 (Linux; Android 14; Pixel 8 Build/AP2A.240905.003) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/148.0.0.0 Mobile Safari/537.36"
            ),
            "clientHints": {"platform": "Android", "mobile": True}
        }

        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(options=options)
        return driver

    yield _create_driver

    if driver:
        driver.quit()
