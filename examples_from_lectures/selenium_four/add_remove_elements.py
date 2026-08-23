import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_add_remove_elements(driver: WebDriver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element_button = driver.find_element(
        By.XPATH, "//button[text()='Add Element']"
    )
    for i in range(3):
        add_element_button.click()
        time.sleep(0.5)

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    for button in delete_buttons:
        button.click()
        time.sleep(0.5)

    remaining_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(remaining_buttons) == 0
