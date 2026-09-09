import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    LOGIN_INPUT = (By.ID, "login-input")
    PASSWORD_INPUT = (By.ID, "password-input")
    LOGIN_BUTTON = (By.ID, "submit-button")
    ERROR_MESSAGE = (By.ID, "error-message")

    @allure.step("Enter your details in the login field.")
    def fill_login(self, login: str):
        self.actions.fill(self.LOGIN_INPUT, login)

    @allure.step("Enter your details in the password field.")
    def fill_password(self, password: str):
        self.actions.fill(self.PASSWORD_INPUT, password)

    @allure.step("Click the login button.")
    def click_login_button(self):
        self.actions.click(self.LOGIN_BUTTON)

    @allure.step("Verify that the error message is correct.")
    def check_error_message(self, message: str) -> bool:
        return self.actions.should_have_text(self.ERROR_MESSAGE, message)
