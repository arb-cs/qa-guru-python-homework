from datetime import datetime
from math import ceil
from pprint import pprint

email = {
    "subject": "Project X: planning integration testing scenarios.",
    "from": "  SeRvice@mail.com  ",
    "to": "  x@qa.COM  ",
    "body": (
        "Hi! We would like to discuss test-cases for integration testing."
        "\nWhen would be the best time for you to meet?\tYours, sincerely Alex"
    ),
}
email["date"] = datetime.now().strftime("%Y-%m-%d")
email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

login, domain = email["from"].split("@")

email["short_body"] = email["body"][:10] + "..."

personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate_domains = list(
    set(
        [
            "company.ru",
            "corporation.com",
            "university.edu",
            "organization.org",
            "company.ru",
            "business.net",
        ]
    )
)

no_common_values = set(personal_domains).isdisjoint(corporate_domains)
is_corporate = email["from"] in corporate_domains

email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")
email["sent_text"] = (
    f"""From: {email["from"]}, To: {email["to"]}, Subject: {email["subject"]},
    Date: {email["date"]} {email["clean_body"]}"""
)

pages = ceil(len(email["sent_text"]) / 500)

is_subject_empty = len(email["subject"].strip()) == 0
is_body_empty = len(email["body"].strip()) == 0

email["masked_from"] = f"{login[:2]}***@{domain}"

personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

pprint(email)
print()
print(
    f"{login =}",
    f"{domain =}",
    f"{personal_domains =}",
    f"{corporate_domains =}",
    f"{no_common_values =}",
    f"{is_corporate =}",
    f"{pages =}",
    f"{is_subject_empty =}",
    f"{is_body_empty =}",
    sep="\n",
)
