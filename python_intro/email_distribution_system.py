import re
import string
from datetime import datetime


def normalize_addresses(address: str) -> str:
    """
    Возвращает значение, в котором адрес приведен к нижнему регистру и очищен от пробелов по краям.
    """
    return address.strip().lower()


def add_short_body(email: dict) -> dict:
    """
    Возвращает email с новым ключом email["short_body"] —
    первые 10 символов тела письма + "...".
    """
    email["short_body"] = email["body"][:10] + "..."
    return email


def clean_body_text(body: str) -> str:
    """
    Заменяет табы и переводы строк на пробелы.
    """
    return re.sub(r"\s+", " ", body).strip()


def build_sent_text(email: dict) -> str:
    """
    Формирует текст письма в формате:

    Кому: {to}, от {from}
    Тема: {subject}, дата {date}
    {clean_body}
    """
    return (
        f"Кому: {email['recipient']}, от {email['sender']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n"
        f"{email['body']}"
    )


def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """
    return not subject or not subject.strip(), not body or not body.strip()


def mask_sender_email(login: str, domain: str) -> str:
    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """
    return f"{login[:2]}***@{domain}"


def get_correct_email(email_list: list[str]) -> list[str]:
    """
    Возвращает список корректных email.
    """
    allowed_domains = (".com", ".ru", ".net")
    allowed_chars = set(string.ascii_letters + string.digits)
    allowed_local_symbols = set("!#$%&'*+-/=?^_{|}~.")
    allowed_domain_symbols = set("-.")

    result = []

    for email in email_list:
        if not email:
            continue

        email = email.strip()

        if "@" not in email or len(email) > 254:
            continue
        if not email.endswith(allowed_domains):
            continue
        if email.startswith("."):
            continue

        try:
            local, domain = email.rsplit("@", 1)
        except ValueError:
            continue

        if (
            not local
            or local.startswith(".")
            or local.endswith(".")
            or ".." in local
        ):
            continue

        for char in local:
            if char not in allowed_chars and char not in allowed_local_symbols:
                break
        else:
            domain_labels = domain.split(".")
            if any(not label for label in domain_labels):
                continue

            valid_domain = True
            for label in domain_labels:
                if label.startswith("-") or label.endswith("-"):
                    valid_domain = False
                    break
                for char in label:
                    if (
                        char not in allowed_chars
                        and char not in allowed_domain_symbols
                    ):
                        valid_domain = False
                        break
                if not valid_domain:
                    break

            if valid_domain:
                result.append(email)

    return result


def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    """
    Создает словарь email с базовыми полями:
    'sender', 'recipient', 'subject', 'body'
    """
    email = {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "body": body,
    }

    return email


def add_send_date(email: dict) -> dict:
    """
    Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
    """
    email["date"] = datetime.now().strftime("%Y-%m-%d")
    return email


def extract_login_domain(address: str) -> tuple[str, str]:
    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
    parts = address.split("@", 1)
    if len(parts) != 2:
        raise ValueError("The email address is not valid!")
    return parts[0], parts[1]


def sender_email(
    recipient_list: list[str],
    subject: str,
    message: str,
    *,
    sender="default@study.com",
) -> list[dict]:
    if not recipient_list:
        raise ValueError("The recipient list is empty!")

    all_addresses = [*recipient_list, sender]
    valid = get_correct_email(all_addresses)

    is_subject_empty, is_body_empty = check_empty_fields(subject, message)
    if is_subject_empty or is_body_empty:
        return []

    valid_recipients = [addr for addr in valid if addr != sender]

    subject = clean_body_text(subject)
    body = clean_body_text(message)
    sender = normalize_addresses(sender)

    result = []
    for recipient in valid_recipients:
        email = create_email(
            sender, normalize_addresses(recipient), subject, body
        )
        email = add_send_date(email)

        login, domain = extract_login_domain(email["sender"])
        email["sender"] = mask_sender_email(login, domain)

        email = add_short_body(email)
        email["sent_text"] = build_sent_text(email)

        result.append(email)

    return result


if __name__ == "__main__":
    recipients = [
        "alex.m@gmail.com",
        "johndoe@x.net",
        "peter_parker@yandex.co.ru",
        "tormund.com",
        "tormund@realnorth.org" " ",
        "nick@.ru",
        "  hello@corp.ru  ",
        "user@site.net",
        "user@domain.com",
        "user@??domain.ru",
        "user.@domain.ru" "..user@domain.com",
    ]
    subject = "Project X: planning integration testing scenarios"
    message = (
        "Hi! We would like to discuss test-cases for integration testing.\n"
        "When would be the best time for you to meet?\tYours, sincerely Alex"
    )

    emails = sender_email(
        recipients, subject, message, sender="alex.m@gmail.com"
    )

    for email in emails:
        print(email)
