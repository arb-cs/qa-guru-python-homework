import pytest

from pages.text_box_page import TextBoxPage


@pytest.mark.regression
def test_fill_text_box(text_box_page: TextBoxPage):
    (
        text_box_page.open()
        .fill_fullname("John Doe")
        .fill_email("john_doe@gmail.com")
        .fill_current_address("740 Route 202 Middletown, NY 10940")
        .fill_permanent_address(
            "9476 Virginia Avenue South Richmond Hill, NY 11419"
        )
        .click_submit_button()
    )

    result = text_box_page.get_output()

    assert result["Name"] == "John Doe"
    assert result["Email"] == "john_doe@gmail.com"
    assert result["Current Address"] == "740 Route 202 Middletown, NY 10940"
    assert (
        result["Permananet Address"]
        == "9476 Virginia Avenue South Richmond Hill, NY 11419"
    )


@pytest.mark.regression
def test_fill_text_box_with_invalid_email(text_box_page: TextBoxPage):
    (
        text_box_page.open()
        .fill_fullname("John Doe")
        .fill_email("?")
        .fill_current_address("740 Route 202 Middletown, NY 10940")
        .fill_permanent_address(
            "9476 Virginia Avenue South Richmond Hill, NY 11419"
        )
        .click_submit_button()
    )

    assert text_box_page.is_result_box_hidden()


@pytest.mark.regression
def test_sql_inject_username_field(text_box_page: TextBoxPage):
    (
        text_box_page.open()
        .fill_fullname("'1' OR '1'='1")
        .fill_email("john_doe@gmail.com")
        .fill_current_address("740 Route 202 Middletown, NY 10940")
        .fill_permanent_address(
            "9476 Virginia Avenue South Richmond Hill, NY 11419"
        )
        .click_submit_button()
    )

    # This check is pointless, and in a real system, a validation error would occur in the username field.
    # However, since there is no validation in this form, let's assume that we're entering the data as-is, but without a successful SQL injection.
    assert text_box_page.is_result_box_visible()
