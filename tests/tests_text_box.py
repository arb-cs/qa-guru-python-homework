import pytest

from pages.text_box_page import TextBoxPage


@pytest.mark.regression
def test_fill_text_box(text_box_page: TextBoxPage):
    # Arrange
    text_box_page.visit()

    # Act
    text_box_page.fill_text_box(
        fullname="John Doe",
        email="john_doe@gmail.com",
        current_address="740 Route 202 Middletown, NY 10940",
        permanent_address="9476 Virginia Avenue South Richmond Hill, NY 11419",
    )
    text_box_page.click_submit_button()

    # Assert
    assert "John Doe" in text_box_page.get_text(text_box_page.NAME_RESULT_BOX)
    assert "john_doe@gmail.com" in text_box_page.get_text(
        text_box_page.EMAIL_RESULT_BOX
    )
    assert "740 Route 202 Middletown, NY 10940" in text_box_page.get_text(
        text_box_page.CURRENT_ADDRESS_RESULT_BOX
    )
    assert (
        "9476 Virginia Avenue South Richmond Hill, NY 11419"
        in text_box_page.get_text(text_box_page.PERMANENT_ADDRESS_RESULT_BOX)
    )


@pytest.mark.regression
def test_fill_text_box_with_invalid_email(text_box_page: TextBoxPage):
    text_box_page.visit()

    text_box_page.fill_text_box(
        fullname="John Doe",
        email="?",
        current_address="740 Route 202 Middletown, NY 10940",
        permanent_address="9476 Virginia Avenue South Richmond Hill, NY 11419",
    )
    text_box_page.click_submit_button()

    assert text_box_page.is_result_box_hidden()


@pytest.mark.regression
def test_sql_inject_username_field(text_box_page: TextBoxPage):
    text_box_page.visit()

    text_box_page.fill_text_box(
        fullname="'1' OR '1'='1",
        email="john_doe@gmail.com",
        current_address="740 Route 202 Middletown, NY 10940",
        permanent_address="9476 Virginia Avenue South Richmond Hill, NY 11419",
    )
    text_box_page.click_submit_button()

    # This check is pointless, and in a real system, a validation error would occur in the username field.
    # However, since there is no validation in this form, let's assume that we're entering the data as-is, but without a successful SQL injection.
    assert text_box_page.is_result_box_visible()
