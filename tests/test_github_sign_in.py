import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "desktop_driver",
    [
        (1280, 800),
        (1440, 900),
        (1920, 1080),
        (320, 568),
        (360, 800)
    ], indirect=True
)
def test_sign_in_desktop(desktop_driver):
    desktop_driver.get("https://github.com/")

    sign_in_button = desktop_driver.find_element(By.XPATH, "//a[contains(@class, 'hiddenBelowLg__BfKBw')]")
    sign_in_button.click()

    page_header = desktop_driver.find_element(By.XPATH, "//h1")

    assert page_header.text == "Sign in to GitHub"


@pytest.mark.parametrize(
    "width, height",
    [
        (320, 568),
        (360, 800),
        (390, 844),
        (1440, 900),
        (1920, 1080)
    ], ids=["iPhone SE", "common Android", "iPhone 12", "desktop", "desktop"]
)
def test_sign_in_mobile(mobile_driver, width, height):
    if width >= 1024:
        pytest.skip("The screen width is not suitable for mobile devices.")

    driver = mobile_driver(width, height)
    driver.get("https://github.com/")

    sign_in_button = driver.find_element(By.XPATH, "(//*[text() ='Sign in'])[1]")
    sign_in_button.click()

    assert driver.title == "Sign in to GitHub · GitHub"
