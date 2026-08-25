import pytest

from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "login, password, error_message",
    [
        ("johndoe@gmail.com", "JoH!?Do1+", "Wrong login or password"),
        (
            "",
            "",
            "Login and password are required (minimum 3 and 6 characters)",
        ),
        ("", "JoH!?Do1+", "Login is required (minimum 3 characters)"),
        ("johndoe", "", "Password is required (minimum 6 characters)"),
    ],
)
def test_unsuccessful_login(
    login_page: LoginPage, login, password, error_message
):
    (
        login_page.open()
        .fill_login(login)
        .fill_password(password)
        .click_login_button()
    )

    assert login_page.check_error_message(error_message)
