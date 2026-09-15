import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from utils import attachments


@pytest.fixture
@allure.title("Instantiate a driver for tests.")
def driver(request, load_env) -> WebDriver:
    remote = request.config.getoption("--selenoid-url")

    if remote:
        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_password = os.getenv("SELENOID_PASSWORD")

        if not selenoid_login or not selenoid_password:
            pytest.fail("No login or password has been specified in the .env file.")

        browser_name = request.config.getoption("--browser")
        browser_version = request.config.getoption("--browser-version")
        is_headless = request.config.getoption("--headless").lower() == "true"
        screen_resolution = request.config.getoption("--screen-resolution")
        screen_resolution = screen_resolution.replace("x", ",")

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser_name == "msedge":
            options = webdriver.EdgeOptions()

        if is_headless:
            options.add_argument("--headless=new")

        options.add_argument(f"--window-size={screen_resolution}")

        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        command_executor = remote.replace(
            "https://",
            f"https://{selenoid_login}:{selenoid_password}@"
        )

        driver = webdriver.Remote(
            command_executor=command_executor,
            options=options
        )

        yield driver

        attachments.add_screenshot(driver)
        attachments.add_console_logs(driver)
        attachments.add_page_source(driver)
        attachments.add_video(driver)

        driver.quit()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()

        yield driver

        driver.quit()
