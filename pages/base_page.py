from pathlib import Path

from selenium.common import ElementNotVisibleException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.EC = EC

    def visit(self):
        self.driver.get(self.url)

    def reload(self):
        self.driver.refresh()

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: tuple[str, str], text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text.strip()

    def should_have_text(self, locator: tuple[str, str], text: str) -> bool:
        return self.get_text(locator) == text

    def is_displayed(self, locator: tuple[str, str]):
        try:
            element = self.wait.until(
                self.EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except ElementNotVisibleException:
            return False

    def count_elements(self, locator: tuple[str, str]):
        elements = self.wait.until(
            (self.EC.visibility_of_all_elements_located(locator))
        )

        return len(elements)

    def scroll_into_view(self, locator: tuple[str, str]) -> WebElement:
        element = self.wait.until(
            self.EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        return element

    def upload_file(self, locator, relative_path: str):
        absolute_path = str(Path(relative_path).resolve())
        element = self.wait.until(self.EC.presence_of_element_located(locator))
        element.send_keys(absolute_path)
