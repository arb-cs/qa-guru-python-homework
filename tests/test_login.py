import allure
import pytest

from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "login, password, error_message",
    [
        ("johndoe@gmail.com", "JoH!?Do1+", "Wrong login or password"),
        ("", "", "Login and password are required (minimum 3 and 6 characters)"),
        ("", "JoH!?Do1+", "Login is required (minimum 3 characters)"),
        ("johndoe", "", "Password is required (minimum 6 characters)"),
    ], ids=["unregistered_user", "empty fields", "empty login", "empty password"]
)
@allure.feature("Authentication")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("This test attempts to log into the system using incorrect credentials.")
def test_unsuccessful_login(login_page: LoginPage, login, password, error_message):
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.click_login_button()

    assert login_page.check_error_message(error_message)
