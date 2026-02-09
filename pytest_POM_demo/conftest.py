import pytest
from selenium import webdriver
from config.browser_settings import BrowserSettings


@pytest.fixture
def configSetting4GobalInOption():
    print("測試前，執行configSetting4GobalInOption前置作業邏輯")
    yield
    print('測試結束，執行configSetting4GobalInOption後置作業邏輯')


@pytest.fixture(scope="session")
def configSetting4Gobal():
    print("測試前，執行configSetting4Gobal前置作業邏輯")
    yield
    print("測試結束，執行configSetting4Gobal後置作業邏輯")


# ------cli指令客製--------


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup_login(browser):
    if 'chrome' == browser:
        driver = BrowserSettings().get_chrome_driver(headless=True)
    elif 'firefox' == browser:
        driver = BrowserSettings().get_firefox_driver(headless=True)
    elif 'edge' == browser:
        driver = BrowserSettings().get_edge_driver(headless=True)
    else:
        driver = BrowserSettings().get_chrome_driver()
    return driver
