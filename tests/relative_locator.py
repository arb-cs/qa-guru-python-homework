import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import locate_with


# Для работы относительных локаторов необходимо импортировать класс with_tag_name (или with_name / with_id) из модуля selenium.webdriver.support.relative_locator.
def test_relative_locator(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    time.sleep(3)
    full_name_label = driver.find_element(
        By.XPATH, "//label[text()='Full Name']"
    )
    full_name_input = driver.find_element(
        locate_with(By.TAG_NAME, "input").to_right_of(full_name_label)
    )
    full_name_input.send_keys("Ivan Ivanov")

    time.sleep(3)
    current_address = driver.find_element(By.ID, "currentAddress")
    email_input = driver.find_element(
        locate_with(By.TAG_NAME, "input").above(current_address)
    )
    email_input.send_keys("ivan@example.com")

    driver.get(
        "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
    )
    time.sleep(3)
    second_radio = driver.find_element(By.ID, "gender-radio-2")
    first_radio = driver.find_element(
        locate_with(By.TAG_NAME, "input").to_left_of(second_radio)
    )
    first_radio.click()

    time.sleep(3)
    first_radio = driver.find_element(By.ID, "gender-radio-1")
    second_radio = driver.find_element(
        locate_with(By.TAG_NAME, "input").to_right_of(first_radio)
    )
    second_radio.click()

    time.sleep(3)
    label_element = driver.find_element(
        By.XPATH, "//label[text()='Current Address']"
    )
    address_textarea = driver.find_element(
        locate_with(By.TAG_NAME, "textarea").near(label_element)
    )
    address_textarea.send_keys("г. Минск, ул. Академическая")
