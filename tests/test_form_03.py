import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("John Doe")

    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("johndoe@gmail.com")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    result_box = driver.find_element(By.ID, "output")

    assert "John Doe" in result_box.text
    assert "johndoe@gmail.com" in result_box.text

    print("Тест успешно пройден!")
finally:
    driver.quit()
