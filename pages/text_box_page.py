import allure
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

    @allure.step("Enter your full name.")
    def fill_fullname(self, fullname: str):
        self.actions.fill(self.FULL_NAME_INPUT, fullname)

    @allure.step("Enter your email.")
    def fill_email(self, email: str):
        self.actions.fill(self.EMAIL_INPUT, email)

    @allure.step("Enter your current address.")
    def fill_current_address(self, current_address: str):
        self.actions.fill(self.CURRENT_ADDRESS_AREA, current_address)

    @allure.step("Enter your permanent address.")
    def fill_permanent_address(self, permanent_address: str):
        self.actions.fill(self.PERMANENT_ADDRESS_AREA, permanent_address)

    @allure.step("Click the submit button.")
    def click_submit_button(self):
        self.actions.click(self.SUBMIT_BUTTON)

    @allure.step("Get the result box.")
    def get_output(self):
        rows = self.actions.find_all(self.RESULT_OUTPUT_ELEMENTS)

        result = {}
        for row in rows:
            key, value = row.text.split(":")
            result[key.strip()] = value

        return result

    @allure.step("Verify that the result box is visible.")
    def is_result_box_visible(self) -> bool:
        try:
            self.actions.find_visible(self.RESULT_BOX)
            return True
        except TimeoutException:
            return False

    @allure.step("Verify that the result box is hidden.")
    def is_result_box_hidden(self) -> bool:
        try:
            self.actions.find_invisible(self.RESULT_BOX)
            return True
        except TimeoutException:
            return False
