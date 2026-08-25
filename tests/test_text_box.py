import pytest

from pages.text_box_page_pf import (
    TextBoxPage,
)


@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        (
            "John Doe",
            "john@example.com",
            "123 Elm St",
            "456 Oak St",
        ),  # Стандартный кейс
        (
            "Иван Иванов",
            "ivan@mail.ru",
            "ул. Ленина, д. 1",
            "ул. Пушкина, д. 2",
        ),  # Кириллица
        ("A", "a@b.cc", "B", "C"),  # Минимальная длина строк
        (
            "Name-With Dash",
            "dash@email.co.uk",
            "Addr 1/2",
            "Addr 3 & 4",
        ),  # Спецсимволы в полях
        (
            "   John   ",
            "spaces@test.com",
            "  Street 1  ",
            "  Street 2  ",
        ),  # Строки с пробелами
    ],
)
def test_positive_form_submission(driver, name, email, cur_addr, perm_addr):
    page = TextBoxPage(driver)

    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()

    output = page.get_output_data()

    assert output, "Блок с результатами не отобразился"
    assert output["name"] == name.strip()
    assert output["email"] == email.strip()
    assert output["cur_addr"] == cur_addr.strip()
    assert output["perm_addr"] == perm_addr.strip()


@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        ("Only Name", "", "", ""),
        ("", "only@email.com", "", ""),
        ("", "", "Only Current Address", ""),
        ("", "", "", "Only Permanent Address"),
        ("Name & Email", "name_email@test.com", "", ""),
    ],
)
def test_partial_form_submission(driver, name, email, cur_addr, perm_addr):
    page = TextBoxPage(driver)

    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()

    output = page.get_output_data()

    assert output["name"] == name
    assert output["email"] == email
    assert output["cur_addr"] == cur_addr
    assert output["perm_addr"] == perm_addr


@pytest.mark.parametrize(
    "invalid_email",
    [
        "plainaddress",
        "@no-local-part.com",
        "john.doe@com",
        "john@missing-dot",
        "john@@example.com",
        "john@example..com",
    ],
)
def test_invalid_email_validation(driver, invalid_email):
    page = TextBoxPage(driver)

    page.open()
    page.fill_form(name="Test", email=invalid_email)
    page.submit()

    # Test will fail for: john.doe@com, john@missing-dot
    assert page.is_email_error_present()


@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        ("A" * 1000, "john@example.com", "Test", "Test"),
        ("John Doe", f"{'b' * 64}@example.com", "Test", "Test"),
        ("John Doe", "john@example.com", "Current " * 200, "Test"),
        ("John Doe", "john@example.com", "Test", "Permanent " * 200),
    ],
)
def test_long_input_fields(driver, name, email, cur_addr, perm_addr):
    page = TextBoxPage(driver)

    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()

    output = page.get_output_data()
    assert output or page.is_email_error_present()


@pytest.mark.parametrize(
    "security_payload",
    [
        "<script>alert('xss')</script>",
        "1' OR '1'='1",
        ":):):):))))::;)",
        "<div>HTML injection</div>",
    ],
)
def test_security_and_special_inputs(driver, security_payload):
    page = TextBoxPage(driver)

    page.open()
    page.fill_form(
        name=security_payload,
        cur_addr=security_payload,
        perm_addr=security_payload,
    )
    page.submit()

    output = page.get_output_data()

    assert output["name"] in security_payload


def test_empty_form_submission(driver):
    page = TextBoxPage(driver)

    page.open()
    page.submit()
    output = page.get_output_data()

    assert output["name"] == ""
    assert output["email"] == ""
