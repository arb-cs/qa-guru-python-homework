from selenium.webdriver.remote.webdriver import WebDriver

from core.driver_actions import DriverActions


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.url = url
        self.driver = driver
        self.actions = DriverActions(driver)

    def open(self):
        if not self.url:
            raise ValueError("Page has not URL defined.")

        self.driver.get(self.url)
        return self

    def reload(self):
        self.driver.refresh()
