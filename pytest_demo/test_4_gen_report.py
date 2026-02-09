import pytest


class TestDemo4PyHtml:

    # 需要安裝pytest-html
    def test_home_page(self, setup):
        self.drive = setup
        self.drive.get("https://www.google.com")
        assert self.drive.title == "Google"
        self.drive.close()

    def test_login_page(self, setup):
        self.drive = setup
        self.drive.get("https://www.google.com")
        assert self.drive.title == "Login"
        self.drive.close()
