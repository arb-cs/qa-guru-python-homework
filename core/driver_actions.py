from pathlib import Path

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DriverActions:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator: tuple[str, str], text: str):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find_visible(locator).text.strip()

    def should_have_text(self, locator: tuple[str, str], text: str) -> bool:
        return self.get_text(locator) == text

    def is_displayed(self, locator: tuple[str, str]):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def count_elements(self, locator: tuple[str, str]):
        elements = self.find_all(locator)
        return len(elements)

    def scroll_into_view(self, locator: tuple[str, str]) -> WebElement:
        element = self.find_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        return element

    def upload_file(self, locator, relative_path: str):
        absolute_path = str(Path(relative_path).resolve())
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(absolute_path)
