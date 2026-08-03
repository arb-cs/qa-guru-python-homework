import pytest

from pages.student_registration_page import StudentRegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_fill_only_required_fields(
    student_registration_page: StudentRegistrationPage,
):
    student_registration_page.visit()

    student_registration_page.fill_only_required_fields(
        "John", "Doe", "Male", "7918123456"
    )
    student_registration_page.close_ad_banner()
    student_registration_page.submit_form()

    assert "John Doe" in student_registration_page.get_text(
        student_registration_page.RESULT_BODY
    )
    assert "7918123456" in student_registration_page.get_text(
        student_registration_page.RESULT_BODY
    )


@pytest.mark.regression
@pytest.mark.registration
def test_fill_all_fields(student_registration_page: StudentRegistrationPage):
    student_registration_page.visit()

    student_registration_page.fill_all_fields(
        "John",
        "Doe",
        "johndoe@gmail.com",
        "Male",
        "7918123456",
        "September",
        "1994",
        "14",
        "Computer Science",
        "Reading",
        "resources/pictures/students.jpg",
        "NYC",
        "NCR",
    )
    student_registration_page.close_ad_banner()
    student_registration_page.submit_form()

    assert student_registration_page.is_result_modal_displayed()
    assert student_registration_page.are_all_rows_on_table(10)
    assert student_registration_page.are_all_fields_filled(
        "John",
        "Doe",
        "johndoe@gmail.com",
        "Male",
        "7918123456",
        "1994-09-14",
        "Computer Science",
        "Reading",
        "students.jpg",
        "NYC",
        "NCR",
    )
