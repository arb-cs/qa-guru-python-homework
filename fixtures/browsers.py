from typing import Any, Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
@allure.title("Instantiate a driver for tests.")
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
