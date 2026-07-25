from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_fill_only_required_fields(driver: WebDriver):
    driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")

    first_name_input = driver.find_element(By.ID, "firstName")
    first_name_input.send_keys("John")

    last_name_input = driver.find_element(By.ID, "lastName")
    last_name_input.send_keys("Doe")

    email_input = driver.find_element(By.ID, "userEmail")
    email_input.send_keys("johndoe@gmail.com")

    gender_radio_button_male = driver.find_element(By.ID, "gender-radio-1")
    gender_radio_button_male.click()

    phone_input = driver.find_element(By.ID, "userNumber")
    phone_input.send_keys("7918123456")

    school_banner = driver.find_element(By.XPATH, "//div[@id = 'siteFooter']//button")
    school_banner.click()

    wait = WebDriverWait(driver, 10)
    submit_form_button = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "submit")))
    submit_form_button.click()

    result_body = driver.find_element(By.ID, "resultBody")

    assert "John Doe" in result_body.text
    assert "johndoe@gmail.com" in result_body.text
    assert "Male" in result_body.text
    assert "7918123456" in result_body.text
