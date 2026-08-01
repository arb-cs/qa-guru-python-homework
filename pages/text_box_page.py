from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_AREA = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_AREA = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    RESULT_BOX = (By.ID, "output")
    NAME_RESULT_BOX = (By.ID, "name")
    EMAIL_RESULT_BOX = (By.ID, "email")
    CURRENT_ADDRESS_RESULT_BOX = (By.CSS_SELECTOR, "p#currentAddress")
    PERMANENT_ADDRESS_RESULT_BOX = (By.CSS_SELECTOR, "p#permanentAddress")

    def fill_text_box(
        self,
        fullname: str,
        email: str,
        current_address: str,
        permanent_address: str,
    ):
        self.type(self.FULL_NAME_INPUT, fullname)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.CURRENT_ADDRESS_AREA, current_address)
        self.type(self.PERMANENT_ADDRESS_AREA, permanent_address)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)

    def is_result_box_visible(self) -> bool:
        try:
            self.wait.until(
                self.EC.visibility_of_element_located(self.RESULT_BOX)
            )
            return True
        except TimeoutException:
            return False

    def is_result_box_hidden(self):
        try:
            self.wait.until(
                self.EC.invisibility_of_element_located(self.RESULT_BOX)
            )
            return True
        except TimeoutException:
            return False
