from selenium.webdriver.common.by import By

from core.driver_actions import DriverActions


class Dropdown:
    def __init__(self, actions: DriverActions, root_locator: tuple[str, str]):
        self.actions = actions
        self.root_locator = root_locator

    def select(self, text: str):
        self.actions.click(self.root_locator)
        option = (By.XPATH, f"//div[text()='{text}']")
        self.actions.scroll_into_view(option)
        self.actions.click(option)
