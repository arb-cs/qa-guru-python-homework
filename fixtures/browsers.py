from typing import Any, Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
@allure.title("Instantiate a driver for tests.")
def driver() -> Generator[WebDriver, Any, None]:
    options = Options()
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.qa.guru/wd/hub",
        options=options
    )

    yield driver

    driver.quit()
