from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_INPUT = (By.ID, "login-input")
    PASSWORD_INPUT = (By.ID, "password-input")
    LOGIN_BUTTON = (By.ID, "submit-button")
    ERROR_MESSAGE = (By.ID, "error-message")

    def fill_login_form(self, login: str, password: str):
        self.type(self.LOGIN_INPUT, login)
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def check_error_message(self, message: str) -> bool:
        return self.should_have_text(self.ERROR_MESSAGE, message)
