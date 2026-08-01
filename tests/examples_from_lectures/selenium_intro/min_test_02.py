import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
driver.maximize_window()

time.sleep(5)
print("Тест успешно пройден!")

driver.quit()
