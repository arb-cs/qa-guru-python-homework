import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.student_registration_page import StudentRegistrationPage
from pages.text_box_page import TextBoxPage


@pytest.fixture
def text_box_page(driver: WebDriver) -> TextBoxPage:
    return TextBoxPage(
        driver, "https://qa-guru.github.io/one-page-form/text-box.html"
    )


@pytest.fixture
def login_page(driver: WebDriver) -> LoginPage:
    return LoginPage(
        driver, "https://qa-guru.github.io/one-page-form/login.html"
    )


@pytest.fixture
def student_registration_page(driver: WebDriver) -> StudentRegistrationPage:
    return StudentRegistrationPage(
        driver,
        "https://qa-guru.github.io/one-page-form/automation-practice-form.html",
    )
