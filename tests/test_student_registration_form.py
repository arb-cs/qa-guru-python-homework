import allure
import pytest

from pages.student_registration_page import StudentRegistrationPage
from utils.dates import format_date


@pytest.mark.regression
@pytest.mark.registration
@allure.feature("Student registration form.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("In this test we check that we can submit the form filling out only the required fields.")
def test_fill_only_required_fields(student_registration_page: StudentRegistrationPage):
    student_registration_page.open()
    student_registration_page.close_ad_banner()
    student_registration_page.set_firstname("John")
    student_registration_page.set_lastname("Doe")
    student_registration_page.set_gender("Male")
    student_registration_page.set_phone("9181234567")
    student_registration_page.submit_form()

    result = student_registration_page.get_result_table()

    assert student_registration_page.is_result_modal_displayed()
    assert result["Student Name"] == "John Doe"
    assert result["Gender"] == "Male"
    assert result["Mobile"] == "9181234567"


@pytest.mark.regression
@pytest.mark.registration
@allure.feature("Student registration form.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("In this test we check that we can fill out all the fields.")
def test_fill_all_fields(student_registration_page: StudentRegistrationPage):
    student_registration_page.open()
    student_registration_page.close_ad_banner()
    student_registration_page.set_firstname("John")
    student_registration_page.set_lastname("Doe")
    student_registration_page.set_email("johndoe@gmail.com")
    student_registration_page.set_gender("Male")
    student_registration_page.set_phone("9181234567")
    student_registration_page.set_birthdate("September", "1994", "14")
    student_registration_page.set_subject("Computer Science")
    student_registration_page.set_hobby("Reading")
    # student_registration_page.upload_picture("resources/pictures/students.jpg")
    student_registration_page.set_current_address("NYC")
    student_registration_page.set_state("NCR")
    student_registration_page.set_city("Delhi")
    student_registration_page.submit_form()

    result = student_registration_page.get_result_table()

    assert student_registration_page.is_result_modal_displayed()
    assert result["Student Name"] == "John Doe"
    assert result["Student Email"] == "johndoe@gmail.com"
    assert result["Gender"] == "Male"
    assert result["Mobile"] == "9181234567"
    assert result["Date of Birth"] == format_date("1994-09-14")
    assert result["Subjects"] == "Computer Science"
    assert result["Hobbies"] == "Reading"
    # assert result["Picture"] == "students.jpg"
    assert result["Address"] == "NYC"
    assert result["State and City"] == "NCR Delhi"
