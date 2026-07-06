from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def test_fill_text_box(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("John Doe")

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("john_doe@gmail.com")

    current_address_area = driver.find_element(By.ID, "currentAddress")
    current_address_area.send_keys("740 Route 202 Middletown, NY 10940")

    permanent_address_area = driver.find_element(By.ID, "permanentAddress")
    permanent_address_area.send_keys(
        "9476 Virginia Avenue South Richmond Hill, NY 11419"
    )

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    name_result_box = driver.find_element(By.ID, "name")
    email_result_box = driver.find_element(By.ID, "email")
    current_address_result_box = driver.find_element(
        By.CSS_SELECTOR, "p#currentAddress"
    )
    permanent_address_result_box = driver.find_element(
        By.CSS_SELECTOR, "p#permanentAddress"
    )

    assert "John Doe" in name_result_box.text
    assert "john_doe@gmail.com" in email_result_box.text
    assert (
        "740 Route 202 Middletown, NY 10940" in current_address_result_box.text
    )
    assert (
        "9476 Virginia Avenue South Richmond Hill, NY 11419"
        in permanent_address_result_box.text
    )


def test_fill_text_box_with_invalid_email(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("John Doe")

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("?")

    current_address_area = driver.find_element(By.ID, "currentAddress")
    current_address_area.send_keys("740 Route 202 Middletown, NY 10940")

    permanent_address_area = driver.find_element(By.ID, "permanentAddress")
    permanent_address_area.send_keys(
        "9476 Virginia Avenue South Richmond Hill, NY 11419"
    )

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    result_box = driver.find_elements(By.CSS_SELECTOR, "div#output > *")

    assert len(result_box) == 0


def test_sql_inject_username_field(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("'1' OR '1'='1")

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("john_doe@gmail.com")

    current_address_area = driver.find_element(By.ID, "currentAddress")
    current_address_area.send_keys("740 Route 202 Middletown, NY 10940")

    permanent_address_area = driver.find_element(By.ID, "permanentAddress")
    permanent_address_area.send_keys(
        "9476 Virginia Avenue South Richmond Hill, NY 11419"
    )

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    result_box = driver.find_elements(By.CSS_SELECTOR, "div#output > *")

    # This check is pointless, and in a real system, a validation error would occur in the username field.
    # However, since there is no validation in this form, let's assume that we're entering the data as-is, but without a successful SQL injection.
    assert len(result_box) > 0
