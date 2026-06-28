from selenium.webdriver.remote.webdriver import WebDriver


def test_open_google_main_page(driver: WebDriver):
    url = "https://www.google.com/"

    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url


def test_open_github_main_page(driver: WebDriver):
    url = "https://github.com/"

    driver.get(url)

    assert (
        driver.title
        == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    )
    assert driver.current_url == url
