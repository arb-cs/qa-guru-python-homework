import pytest

from pages.login_page import LoginPage


# All these tests are quite similar. Parametrize?
@pytest.mark.regression
@pytest.mark.authorization
def test_unsuccessful_login(login_page: LoginPage):
    login_page.visit()

    login_page.fill_login_form("johndoe@gmail.com", "JoH!?Do1+")
    login_page.click_login_button()

    assert login_page.check_error_message("Wrong login or password")


@pytest.mark.regression
@pytest.mark.authorization
def test_submit_empty_login_form(login_page: LoginPage):
    login_page.visit()

    login_page.fill_login_form("", "")
    login_page.click_login_button()

    assert login_page.check_error_message(
        "Login and password are required (minimum 3 and 6 characters)"
    )


@pytest.mark.regression
@pytest.mark.authorization
def test_submit_empty_login_input(login_page: LoginPage):
    login_page.visit()

    login_page.fill_login_form("", "JoH!?Do1+")
    login_page.click_login_button()

    assert login_page.check_error_message(
        "Login is required (minimum 3 characters)"
    )


@pytest.mark.regression
@pytest.mark.authorization
def test_submit_empty_password_input(login_page: LoginPage):
    login_page.visit()

    login_page.fill_login_form("johndoe", "")
    login_page.click_login_button()

    assert login_page.check_error_message(
        "Password is required (minimum 6 characters)"
    )
