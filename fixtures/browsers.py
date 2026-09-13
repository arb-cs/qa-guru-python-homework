from typing import Any, Generator

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from utils import attachments


@pytest.fixture
@allure.title("Instantiate a driver for tests.")
def driver() -> Generator[WebDriver, Any, None]:
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "152.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.qa.guru/wd/hub",
        options=options
    )

    yield driver

    attachments.add_screenshot(driver)
    attachments.add_video(driver)
    attachments.add_console_logs(driver)
    attachments.add_page_source(driver)

    driver.quit()
