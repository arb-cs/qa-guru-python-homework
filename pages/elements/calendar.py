from calendar import month_name
from datetime import datetime

from selenium.webdriver.common.by import By


class Calendar:
    def __init__(self, page, month: str, year: str, day: str):
        self.page = page

        if month not in list(month_name[1:]):
            raise ValueError("Invalid month name")

        year = int(year)
        if year < 1900 or year > 2100:
            raise ValueError("Year must be between 1900 and 2100")

        day = int(day)
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        self.month = month
        self.year = year
        self.day = day

    @property
    def month_locator(self):
        return (
            By.XPATH,
            f"//select[@class='react-datepicker__month-select']//option[text()='{self.month}']",
        )

    @property
    def year_locator(self):
        return (
            By.XPATH,
            f"//select[@class='react-datepicker__year-select']//option[text()='{self.year}']",
        )

    @property
    def day_locator(self):
        return (
            By.XPATH,
            f"//div[@id='datepickerDays']//span[text()='{self.day}']",
        )

    def set_date(self):
        self.page.click(self.month_locator)
        self.page.click(self.year_locator)
        self.page.click(self.day_locator)

    @staticmethod
    def format_date(date: str) -> str:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return date_obj.strftime("%d %b %Y")
