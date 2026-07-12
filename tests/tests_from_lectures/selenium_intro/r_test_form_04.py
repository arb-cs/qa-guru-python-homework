import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test01():
    print("Рефакторинг - итерация 1!")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Test Test")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("test@example.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "Test Test" in result_box.text
        assert "test@example.com" in result_box.text

        print("Тест успешно пройден!")

    finally:
        driver.quit()


def test02():
    print("Рефакторинг - итерация 1!")

    driver = webdriver.Chrome()

    try:
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)

        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("")

        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("qa_testing@gmail.com")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(5)

        result_box = driver.find_element(By.ID, "output")

        assert "qa_testing@gmail.com" in result_box.text
        print("Тест успешно пройден!")
    finally:
        driver.quit()
