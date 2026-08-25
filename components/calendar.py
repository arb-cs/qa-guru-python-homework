from calendar import month_name

from selenium.webdriver.common.by import By

from core.driver_actions import DriverActions


class Calendar:
    def __init__(self, actions: DriverActions):
        self.actions = actions

    def set_date(self, month: str, year: str, day: str):
        if month not in list(month_name[1:]):
            raise ValueError("Invalid select_month name")

        year = int(year)
        if year < 1900 or year > 2100:
            raise ValueError("Year must be between 1900 and 2100")

        day = int(day)
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1 and 31")

        select_month = (
            By.XPATH,
            f"//select[@class='react-datepicker__month-select']//option[text()='{month}']",
        )
        select_year = (
            By.XPATH,
            f"//select[@class='react-datepicker__year-select']//option[text()='{year}']",
        )
        select_day = (
            By.XPATH,
            f"//div[@id='datepickerDays']//span[text()='{day}']",
        )

        self.actions.click(select_month)
        self.actions.click(select_year)
        self.actions.click(select_day)
