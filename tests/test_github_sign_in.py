import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

WINDOW_SIZES = [
    (1280, 800),
    (1440, 900),
    (1920, 1080),
    (320, 568),
    (360, 800),
    (390, 844)
]


@pytest.mark.parametrize(
    "desktop_driver",
    WINDOW_SIZES,
    indirect=True
)
def test_sign_in_desktop(desktop_driver: WebDriver):
    desktop_driver.get("https://github.com/")

    sign_in_button = desktop_driver.find_element(By.XPATH, "//a[contains(@class, 'hiddenBelowLg__BfKBw')]")
    sign_in_button.click()

    page_header = desktop_driver.find_element(By.XPATH, "//h1")

    assert page_header.text == "Sign in to GitHub"


@pytest.mark.parametrize(
    "mobile_driver",
    WINDOW_SIZES,
    indirect=True
)
def test_sign_in_mobile(mobile_driver: WebDriver):
    mobile_driver.get("https://github.com/")

    sign_in_button = mobile_driver.find_element(By.XPATH, "(//*[text() ='Sign in'])[1]")
    sign_in_button.click()

    assert mobile_driver.title == "Sign in to GitHub · GitHub"
