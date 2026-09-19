import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.student_registration_page import StudentRegistrationPage
from pages.text_box_page import TextBoxPage


def build_url(base, path):
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
@allure.title("Create an instance of TextBoxPage class.")
def text_box_page(driver: WebDriver, base_url) -> TextBoxPage:
    url = build_url(base_url, "one-page-form/text-box.html")
    return TextBoxPage(driver, url)


@pytest.fixture
@allure.title("Create an instance of LoginPage class.")
def login_page(driver: WebDriver, base_url) -> LoginPage:
    url = build_url(base_url, "one-page-form/login.html")
    return LoginPage(driver, url)


@pytest.fixture
@allure.title("Create an instance of StudentRegistrationPage class.")
def student_registration_page(driver: WebDriver, base_url) -> StudentRegistrationPage:
    url = build_url(base_url, "one-page-form/automation-practice-form.html")
    return StudentRegistrationPage(driver, url)
