import pytest

from pages.student_registration_page import StudentRegistrationPage
from utils.dates import format_date


@pytest.mark.regression
@pytest.mark.registration
def test_fill_only_required_fields(
    student_registration_page: StudentRegistrationPage,
):
    (
        student_registration_page.open()
        .set_firstname("John")
        .set_lastname("Doe")
        .set_gender("Male")
        .set_phone("9181234567")
        .close_ad_banner()
        .submit_form()
    )

    result = student_registration_page.get_result_table()

    assert student_registration_page.is_result_modal_displayed()
    assert result["Student Name"] == "John Doe"
    assert result["Gender"] == "Male"
    assert result["Mobile"] == "9181234567"


@pytest.mark.regression
@pytest.mark.registration
def test_fill_all_fields(student_registration_page: StudentRegistrationPage):
    (
        student_registration_page.open()
        .set_firstname("John")
        .set_lastname("Doe")
        .set_email("johndoe@gmail.com")
        .set_gender("Male")
        .set_phone("9181234567")
        .set_birthdate("September", "1994", "14")
        .set_subject("Computer Science")
        .set_hobby("Reading")
        .upload_picture("resources/pictures/students.jpg")
        .set_current_address("NYC")
        .set_state("NCR")
        .set_city("Delhi")
        .close_ad_banner()
        .submit_form()
    )

    result = student_registration_page.get_result_table()

    assert student_registration_page.is_result_modal_displayed()
    assert result["Student Name"] == "John Doe"
    assert result["Student Email"] == "johndoe@gmail.com"
    assert result["Gender"] == "Male"
    assert result["Mobile"] == "9181234567"
    assert result["Date of Birth"] == format_date("1994-09-14")
    assert result["Subjects"] == "Computer Science"
    assert result["Hobbies"] == "Reading"
    assert result["Picture"] == "students.jpg"
    assert result["Address"] == "NYC"
    assert result["State and City"] == "NCR Delhi"
