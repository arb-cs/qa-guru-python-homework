from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.elements.calendar import Calendar


class StudentRegistrationPage(BasePage):
    SUBJECTS_LIST = [
        "Maths",
        "Physics",
        "Chemistry",
        "Biology",
        "English",
        "Computer Science",
        "Economics",
        "Arts",
        "History",
        "Civics",
    ]

    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    USER_EMAIL_INPUT = (By.ID, "userEmail")
    USER_NUMBER_INPUT = (By.ID, "userNumber")
    BIRTHDAY_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    HOBBIES_WRAPPER = (By.ID, "hobbiesWrapper")
    UPLOAD_PICTURE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_AREA = (By.ID, "currentAddress")
    STATE_COMBOBOX = (By.ID, "state")
    CITY_COMBOBOX = (By.ID, "city")
    CITY = (
        By.XPATH,
        "//*[@id='stateCity-wrapper']/div[1]",
    )  # For now, let's temporarily select the first city from the list
    CLOSE_BANNER_BUTTON = (By.XPATH, "//div[@id = 'fixedban']//button")
    SUBMIT_BUTTON = (By.ID, "submit")
    RESULT_MODAL = (By.ID, "resultModal")
    RESULT_BODY = (By.ID, "resultBody")
    RESULT_TABLE_ELEMENTS = (By.XPATH, "//*[@id='resultBody']//tr")

    def close_ad_banner(self):
        self.click(self.CLOSE_BANNER_BUTTON)

    def set_gender(self, gender: str):
        if gender not in ("Male", "Female", "Other"):
            raise ValueError("A gender must by one of: Male, Female, Other")
        self.click(
            (
                By.XPATH,
                f"//div[@id = 'genterWrapper']//input[@value = '{gender}']",
            )
        )

    def set_birthdate(self, month, year, day):
        self.click(self.BIRTHDAY_INPUT)

        calendar = Calendar(self, month, year, day)
        calendar.set_date()

    def set_subject(self, subject: str):
        if subject not in self.SUBJECTS_LIST:
            raise ValueError("Invalid subject.")

        subject_choice = (
            By.XPATH,
            f"//div[@id = 'subjectsDropdown']//div[text() = '{subject}']",
        )

        self.click(self.SUBJECTS_INPUT)
        self.scroll_into_view(subject_choice)
        self.click(subject_choice)

    def set_hobbies(self, hobby: str):
        if hobby not in ("Sports", "Reading", "Music"):
            raise ValueError("Invalid hobby.")

        self.click(
            (
                By.XPATH,
                f"//div[@id = 'hobbiesWrapper']//label//input[@value = '{hobby}']",
            )
        )

    def upload_picture(self, relative_path: str):
        self.upload_file(self.UPLOAD_PICTURE_INPUT, relative_path)

    def set_state(self, state: str):
        if state not in ("NCR", "Uttar Pradesh", "Haryana", "Rajasthan"):
            raise ValueError("Invalid state.")

        self.click(self.STATE_COMBOBOX)
        state_choice = (
            By.XPATH,
            f"//div[@id='stateCity-wrapper']/div[text() = '{state}']",
        )
        self.scroll_into_view(state_choice)
        self.click(state_choice)

    def set_city(self):
        self.click(self.CITY_COMBOBOX)
        self.click(self.CITY)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)

    def get_result_table(self) -> dict:
        rows = self.driver.find_elements(*self.RESULT_TABLE_ELEMENTS)
        result = {}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            result[key] = value

        return result

    def fill_only_required_fields(
        self, firstname: str, lastname: str, gender: str, phone: str
    ):
        self.type(self.FIRSTNAME_INPUT, firstname)
        self.type(self.LASTNAME_INPUT, lastname)
        self.set_gender(gender)
        self.type(self.USER_NUMBER_INPUT, phone)

    def fill_all_fields(
        self,
        firstname: str,
        lastname: str,
        email: str,
        gender: str,
        phone: str,
        month: str,
        year: str,
        day: str,
        subject: str,
        hobby: str,
        picture_relative_path: str,
        current_address: str,
        state: str,
    ):
        self.type(self.FIRSTNAME_INPUT, firstname)
        self.type(self.LASTNAME_INPUT, lastname)
        self.type(self.USER_EMAIL_INPUT, email)
        self.set_gender(gender)
        self.type(self.USER_NUMBER_INPUT, phone)
        self.set_birthdate(month, year, day)
        self.set_subject(subject)
        self.set_hobbies(hobby)
        self.upload_picture(picture_relative_path)
        self.type(self.CURRENT_ADDRESS_AREA, current_address)
        self.set_state(state)
        self.set_city()

    def is_result_modal_displayed(self) -> bool:
        return self.is_displayed(self.RESULT_MODAL)

    def are_all_rows_on_table(self, number: int) -> bool:
        return self.count_elements(self.RESULT_TABLE_ELEMENTS) == number

    def are_all_fields_filled(
        self,
        firstname: str,
        lastname: str,
        email: str,
        gender: str,
        phone: str,
        birthdate: str,
        subject: str,
        hobby: str,
        picture: str,
        current_address: str,
        state: str,
    ):

        expected = {
            "Student Name": f"{firstname} {lastname}",
            "Student Email": email,
            "Gender": gender,
            "Mobile": phone,
            "Date of Birth": Calendar.format_date(birthdate),
            "Subjects": subject,
            "Hobbies": hobby,
            "Picture": picture,
            "Address": current_address,
            "State and City": f"{state} {self.get_text(self.CITY_COMBOBOX)}",
        }

        actual = self.get_result_table()

        return actual == expected
