from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_drag_and_drop(driver: WebDriver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    source_element = driver.find_element(By.ID, "column-a")
    target_element = driver.find_element(By.ID, "column-b")

    actions = ActionChains(driver)

    actions.drag_and_drop(source_element, target_element).perform()
    actions.drag_and_drop(target_element, source_element).perform()
