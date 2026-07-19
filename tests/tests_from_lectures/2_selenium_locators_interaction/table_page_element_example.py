import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self):
        return self.driver.find_element(*self.locator)

    def get_headers(self) -> list[str]:
        """Возвращает список заголовков таблицы."""
        header_elements = self.element.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        """Возвращает данные конкретной строки по её индексу (начиная с 0)."""
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        """Возвращает значение конкретной ячейки."""
        cells = self.get_row_data(row_index)
        return cells[column_index]


def test_original(driver: WebDriver):
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")

    # Инициализация таблицы как Page Element через её локатор
    table1_locator = (By.ID, "table1")
    table = TableElement(driver, table1_locator)

    # Сбор данных для демонстрации
    headers = table.get_headers()
    first_row = table.get_row_data(0)
    specific_cell = table.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)

    # Вывод результатов в консоль
    print("Заголовки таблицы:", headers)
    print("Первая строка данных:", first_row)
    print(f"Значение в строке 3, колонке 'Due': {specific_cell}")

    # Простые проверки (Assertions)
    assert "Last Name" in headers, "Заголовок 'Last Name' не найден"
    assert "Smith" in first_row, "Фамилия 'Smith' должна быть в первой строке"
    assert specific_cell == "$100.00", f"Ожидалось $100.00, но получено {specific_cell}"

    print("\n✅ Тест успешно пройден!")
    time.sleep(5)


def test_second_table(driver: WebDriver):
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")

    last_name = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) td.last-name")
    first_name = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) td.first-name")
    email = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) td.email")
    due = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) td.dues")
    web_site = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) td.web-site")

    assert last_name.text == "Smith"
    assert first_name.text == "John"
    assert email.text == "jsmith@gmail.com"
    assert due.text == "$50.00"
    assert web_site.text == "http://www.jsmith.com"


def test_both_tables(driver: WebDriver):
    driver.implicitly_wait(5)
    driver.get("https://the-internet.herokuapp.com/tables")

    last_name_first_table = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td[1]")
    first_name_first_table = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td[2]")

    last_name_second_table = driver.find_element(By.XPATH, "//table[@id='table2']/tbody/tr[1]/td[1]")
    first_name_second_table = driver.find_element(By.XPATH, "//table[@id='table2']/tbody/tr[1]/td[2]")

    assert last_name_first_table.text == last_name_second_table.text
    assert first_name_first_table.text == first_name_second_table.text
