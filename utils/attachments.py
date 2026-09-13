import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver


def add_screenshot(driver: WebDriver) -> None:
    png = driver.get_screenshot_as_png()
    allure.attach(body=png, name="screenshot", attachment_type=AttachmentType.PNG, extension=".png")


def add_video(driver: WebDriver) -> None:
    video_url = "https://selenoid.qa.guru/video/" + driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, "video_" + driver.session_id, AttachmentType.HTML, extension=".html")


def add_console_logs(driver: WebDriver) -> None:
    logs = "".join(f"{text}\n" for text in driver.execute("getLog", {"type": "browser"})["value"])
    allure.attach(logs, "browser_logs", AttachmentType.TEXT, extension=".log")


def add_page_source(driver: WebDriver) -> None:
    page_source = driver.page_source
    allure.attach(page_source, "page_source", AttachmentType.HTML, extension=".page_source")
