from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_unsuccessful_login(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    login_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'login-input']")
    login_input.send_keys("johndoe@gmail.com")

    password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'password-input']")
    password_input.send_keys("JoH!?Do1+")

    login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'submit-button']")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'error-message']")

    assert error_message.text == "Wrong login or password"


def test_submit_empty_login_form(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    login_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'login-input']")
    login_input.send_keys("")

    password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'password-input']")
    password_input.send_keys("")

    login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'submit-button']")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'error-message']")

    assert error_message.text == "Login and password are required (minimum 3 and 6 characters)"


def test_submit_empty_login_input(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    login_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'login-input']")
    login_input.send_keys("")

    password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'password-input']")
    password_input.send_keys("JoH!?Do1+")

    login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'submit-button']")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'error-message']")

    assert error_message.text == "Login is required (minimum 3 characters)"


def test_submit_empty_password_input(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/login.html")

    login_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'login-input']")
    login_input.send_keys("johndoe")

    password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'password-input']")
    password_input.send_keys("")

    login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'submit-button']")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid = 'error-message']")

    assert error_message.text == "Password is required (minimum 6 characters)"
