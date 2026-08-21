from selenium.webdriver.common.by import By

from core.driver_actions import DriverActions


class CheckBox:
    def __init__(self, actions: DriverActions, root_locator: tuple[str, str]):
        self.actions = actions
        self.root_locator = root_locator

    def select(self, value):
        locator = (By.XPATH, f"{self.root_locator[1]}//input[@value='{value}']")
        self.actions.click(locator)
