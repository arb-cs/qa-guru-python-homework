from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
