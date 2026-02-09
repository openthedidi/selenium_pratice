import pytest
import selenium
from config.browser_settings import BrowserSettings
from config.log_settings import setup_logging


class TestDemo4Parallel:

    # 需要先安裝pytest-xdist
    # 指令python -m  pytest -v -s -n={批次執行測試的數量} .\pytest_demo\test_4_parallel.py

    def test_login_by_chrome(self):
        self.driver = BrowserSettings().get_chrome_driver(
            headless=True)
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        self.driver.quit()

    def test_login_by_edge(self):
        self.driver = BrowserSettings().get_edge_driver(
            headless=True)
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        self.driver.quit()

    def test_login_by_firefox(self):
        self.driver = BrowserSettings().get_edge_driver(
            headless=True)
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        self.driver.quit()

        assert True

    def test_login_by_cli(self, setup):
        self.driver = setup
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        self.driver.quit()
