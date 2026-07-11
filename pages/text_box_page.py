from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.full_name_field = driver.find_element(By.ID, "userName")
        self.email_field = driver.find_element(By.ID, "userEmail")
        self.current_address_area = driver.find_element(By.ID, "currentAddress")
        self.permanent_address_area = driver.find_element(
            By.ID, "permanentAddress"
        )
        self.submit_button = driver.find_element(By.ID, "submit")
        self.name_result_box = driver.find_element(By.ID, "name")
        self.email_result_box = driver.find_element(By.ID, "email")
        self.current_address_result_box = driver.find_element(
            By.CSS_SELECTOR, "p#currentAddress"
        )
        self.permanent_address_result_box = driver.find_element(
            By.CSS_SELECTOR, "p#permanentAddress"
        )

    def fill_text_box(
        self,
        fullname: str,
        email: str,
        current_address: str,
        permanent_address: str,
    ):
        self.full_name_field.send_keys(fullname)
        self.email_field.send_keys(email)
        self.current_address_area.send_keys(current_address)
        self.permanent_address_area.send_keys(permanent_address)

    def click_submit_button(self):
        self.submit_button.click()

    def check_form_was_filled(
        self,
        fullname: str,
        email: str,
        current_address: str,
        permanent_address: str,
    ):
        assert fullname in self.name_result_box
        assert email in self.email_result_box
        assert current_address in self.current_address_result_box
        assert permanent_address in self.permanent_address_result_box
