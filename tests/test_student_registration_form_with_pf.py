import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    def open_url(self, url: str):
        self.driver.get(url)


class AutomationPracticeFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "first_name": ("ID", "firstName"),
        "last_name": ("ID", "lastName"),
        "user_email": ("ID", "userEmail"),
        "banner_button": (
            "XPATH",
            "//div[@id='fixedban']//button[@aria-label='Close']",
        ),
        "gender_male": ("XPATH", "//label[@for='gender-radio-1']"),
        "gender_female": ("XPATH", "//label[@for='gender-radio-2']"),
        "gender_other": ("XPATH", "//label[@for='gender-radio-3']"),
        "user_number": ("ID", "userNumber"),
        "date_of_birth_input": ("ID", "dateOfBirthInput"),
        "calendar_month_select": (
            "CLASS_NAME",
            "react-datepicker__month-select",
        ),
        "calendar_year_select": ("CLASS_NAME", "react-datepicker__year-select"),
        "subjects_input": ("ID", "subjectsInput"),
        "subjects_auto_complete_option": (
            "XPATH",
            "//div[contains(@class, 'subjects-auto-complete__option')]",
        ),
        "hobby_sports": ("XPATH", "//label[@for='hobbies-checkbox-1']"),
        "hobby_reading": ("XPATH", "//label[@for='hobbies-checkbox-2']"),
        "hobby_music": ("XPATH", "//label[@for='hobbies-checkbox-3']"),
        "upload_picture_btn": ("ID", "uploadPicture"),
        "current_address": ("ID", "currentAddress"),
        "state_dropdown": ("ID", "state"),
        "state_input": ("XPATH", "//div[@id='state']//input"),
        "city_dropdown": ("ID", "city"),
        "city_input": ("XPATH", "//div[@id='city']//input"),
        "submit_button": ("ID", "submit"),
        "modal_title": ("ID", "example-modal-sizes-title-lg"),
        "modal_table_rows": ("XPATH", "//*[@id='resultBody']//tr"),
    }

    def close_commercial_banner(self):
        self.banner_button.click()

    def set_first_name(self, first_name):
        self.first_name.set_text(first_name)

    def set_last_name(self, last_name):
        self.last_name.set_text(last_name)

    def set_email(self, email):
        self.user_email.set_text(email)

    def set_gender(self, gender):
        if gender.lower() == "male":
            self.gender_male.click_button()
        elif gender.lower() == "female":
            self.gender_female.click_button()
        else:
            self.gender_other.click_button()

    def set_phone_number(self, phone_number):
        self.user_number.set_text(phone_number)

    def select_date_of_birth(self, year: str, month: str, day: str):
        self.date_of_birth_input.click_button()

        self.calendar_year_select.select_element_by_value(year)
        self.calendar_month_select.select_element_by_text(month)

        day_element = self.driver.find_element(
            By.XPATH, f"//div[@id='datepickerDays']//span[text()='{day}']"
        )
        day_element.click()

    def enter_subjects(self, subjects: list):
        for subject in subjects:
            self.subjects_input.set_text(subject)
            self.subjects_input.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies: list):
        hobbies_map = {
            "sports": self.hobby_sports,
            "reading": self.hobby_reading,
            "music": self.hobby_music,
        }
        for hobby in hobbies:
            hobby_lower = hobby.lower()
            if hobby_lower in hobbies_map:
                print(hobbies_map[hobby_lower])
                hobbies_map[hobby_lower].click_button()

    def upload_file(self, file_path: str):
        self.upload_picture_btn.send_keys(file_path)

    def fill_address_and_location(self, address: str, state: str, city: str):
        wait = WebDriverWait(self.driver, 10)
        self.current_address.set_text(address)

        wait.until(EC.element_to_be_clickable((By.ID, "state"))).click()
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@id='stateCity-wrapper']//div[text()='{state}']",
                )
            )
        ).click()

        wait.until(EC.element_to_be_clickable((By.ID, "city"))).click()
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@id='stateCity-wrapper']//div[text()='{city}']",
                )
            )
        ).click()

    def submit_form(self):
        self.driver.execute_script("arguments[0].click();", self.submit_button)

    def get_modal_results(self) -> dict:
        rows = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//*[@id='resultBody']//tr")
            )
        )

        result_data = {}
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            label = cells[0].text.strip()
            value = cells[1].text.strip()
            result_data[label] = value

        return result_data


def test_student_registration_form_max_capabilities(driver):
    test_filename = "demo_upload.txt"
    with open(test_filename, "w") as f:
        f.write("QA Guru PageFactory Demo File Content")
    abs_file_path = os.path.abspath(test_filename)

    page = AutomationPracticeFormPage(driver)
    page.open_url(
        "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
    )

    page.close_commercial_banner()
    page.set_first_name("Ivan")
    page.set_last_name("Ivanov")
    page.set_email("ivanov@university.edu")
    page.set_gender("male")
    page.set_phone_number("1234567890")
    page.select_date_of_birth(year="2000", month="January", day="15")
    page.enter_subjects(subjects=["Maths", "Computer Science"])
    page.select_hobbies(hobbies=["Sports", "Music"])
    page.upload_file(file_path=abs_file_path)
    page.fill_address_and_location(
        address="123 University Avenue, Tomsk, Russia",
        state="NCR",
        city="Delhi",
    )
    page.submit_form()

    actual_results = page.get_modal_results()

    assert (
        actual_results.get("Student Name") == "Ivan Ivanov"
    ), f"Ожидалось имя 'Ivan Ivanov', получено: {actual_results.get('Student Name')}"
    assert actual_results.get("Student Email") == "ivanov@university.edu"
    assert actual_results.get("Gender") == "Male"
    assert actual_results.get("Mobile") == "1234567890"
    assert actual_results.get("Date of Birth") == "15 Jan 2000"
    assert actual_results.get("Subjects") == "Maths, Computer Science"
    assert actual_results.get("Hobbies") == "Sports, Music"
    assert actual_results.get("Picture") == test_filename
    assert (
        actual_results.get("Address") == "123 University Avenue, Tomsk, Russia"
    )
    assert actual_results.get("State and City") == "NCR Delhi"

    if os.path.exists(abs_file_path):
        os.remove(abs_file_path)
