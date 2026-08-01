from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_remove_checkbox(driver: WebDriver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    wait = WebDriverWait(driver, 10)

    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox input")

    remove_checkbox_button = driver.find_element(
        By.XPATH, "//form[@id = 'checkbox-example']//button"
    )
    remove_checkbox_button.click()

    assert wait.until(EC.invisibility_of_element(checkbox))


def test_click_enable(driver: WebDriver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    wait = WebDriverWait(driver, 10)

    enable_button = driver.find_element(
        By.CSS_SELECTOR, "#input-example button"
    )
    enable_button.click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))

    assert message.text == "It's enabled!"
