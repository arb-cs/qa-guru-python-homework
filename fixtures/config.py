import os

import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--base-url", default="https://qa-guru.github.io/")
    parser.addoption("--selenoid-url", default=None)
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox", "msedge"))
    parser.addoption("--browser-version", default="148.0")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--screen-resolution", default="1920x1080",
                     choices=("1366x768", "1440x900", "1920x1080", "2560x1440"))
    parser.addoption("--environment", default=None)


@pytest.fixture(scope="session")
def load_env(request):
    env = request.config.getoption("--environment")
    if not env:
        return

    env_file = f"{env}.env"

    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        pytest.fail(f"Environment file '{env_file}' not found.")
