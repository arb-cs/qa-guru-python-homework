from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.calendar import Calendar
from components.checkbox import CheckBox
from components.dropdown import Dropdown
from pages.base_page import BasePage


class StudentRegistrationPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)
        self.gender_checkbox = CheckBox(self.actions, self.GENDER_WRAPPER)
        self.calendar = Calendar(self.actions)
        self.subjects_dropdown = Dropdown(self.actions, self.SUBJECTS_INPUT)
        self.hobbies_checkbox = CheckBox(self.actions, self.HOBBIES_WRAPPER)
        self.state_dropdown = Dropdown(self.actions, self.STATE_COMBOBOX)
        self.city_dropdown = Dropdown(self.actions, self.CITY_COMBOBOX)

    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    USER_EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_WRAPPER = (By.XPATH, "//*[@id = 'genterWrapper']")
    PHONE_NUMBER_INPUT = (By.ID, "userNumber")
    BIRTHDAY_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    HOBBIES_WRAPPER = (By.XPATH, "//*[@id = 'hobbiesWrapper']")
    UPLOAD_PICTURE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_AREA = (By.ID, "currentAddress")
    STATE_COMBOBOX = (By.ID, "state")
    CITY_COMBOBOX = (By.ID, "city")
    CLOSE_BANNER_BUTTON = (By.XPATH, "//div[@id = 'fixedban']//button")
    SUBMIT_BUTTON = (By.ID, "submit")
    RESULT_MODAL = (By.ID, "resultModal")
    RESULT_TABLE_ELEMENTS = (By.XPATH, "//*[@id='resultBody']//tr")

    def set_firstname(self, firstname: str):
        self.actions.fill(self.FIRSTNAME_INPUT, firstname)
        return self

    def set_lastname(self, lastname: str):
        self.actions.fill(self.LASTNAME_INPUT, lastname)
        return self

    def set_email(self, email: str):
        self.actions.fill(self.USER_EMAIL_INPUT, email)
        return self

    def set_phone(self, phone: str):
        self.actions.fill(self.PHONE_NUMBER_INPUT, phone)
        return self

    def set_gender(self, gender: str):
        self.gender_checkbox.select(gender)
        return self

    def set_birthdate(self, month, year, day):
        self.actions.click(self.BIRTHDAY_INPUT)
        self.calendar.set_date(month, year, day)
        return self

    def set_subject(self, subject: str):
        self.subjects_dropdown.select(subject)
        return self

    def set_hobby(self, hobby: str):
        self.hobbies_checkbox.select(hobby)
        return self

    def upload_picture(self, relative_path: str):
        self.actions.upload_file(self.UPLOAD_PICTURE_INPUT, relative_path)
        return self

    def set_current_address(self, address: str):
        self.actions.fill(self.CURRENT_ADDRESS_AREA, address)
        return self

    def set_state(self, state: str):
        self.state_dropdown.select(state)
        return self

    def set_city(self, city: str):
        self.city_dropdown.select(city)
        return self

    def close_ad_banner(self):
        self.actions.click(self.CLOSE_BANNER_BUTTON)
        return self

    def submit_form(self):
        self.actions.click(self.SUBMIT_BUTTON)
        return self

    def get_result_table(self) -> dict:
        rows = self.actions.find_all(self.RESULT_TABLE_ELEMENTS)
        result = {}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            result[key] = value

        return result

    def is_result_modal_displayed(self) -> bool:
        return self.actions.is_displayed(self.RESULT_MODAL)
