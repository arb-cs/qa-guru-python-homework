from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_AREA = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_AREA = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    RESULT_BOX = (By.ID, "output")
    RESULT_OUTPUT_ELEMENTS = (By.XPATH, "//div[@id = 'output']//p")

    def fill_fullname(self, fullname: str):
        self.actions.fill(self.FULL_NAME_INPUT, fullname)
        return self

    def fill_email(self, email: str):
        self.actions.fill(self.EMAIL_INPUT, email)
        return self

    def fill_current_address(self, current_address: str):
        self.actions.fill(self.CURRENT_ADDRESS_AREA, current_address)
        return self

    def fill_permanent_address(self, permanent_address: str):
        self.actions.fill(self.PERMANENT_ADDRESS_AREA, permanent_address)
        return self

    def click_submit_button(self):
        self.actions.click(self.SUBMIT_BUTTON)

    def get_output(self):
        rows = self.actions.find_all(self.RESULT_OUTPUT_ELEMENTS)

        result = {}
        for row in rows:
            key, value = row.text.split(":")
            result[key.strip()] = value

        return result

    def is_result_box_visible(self) -> bool:
        try:
            self.actions.find_visible(self.RESULT_BOX)
            return True
        except TimeoutException:
            return False

    def is_result_box_hidden(self) -> bool:
        try:
            self.actions.find_invisible(self.RESULT_BOX)
            return True
        except TimeoutException:
            return False
