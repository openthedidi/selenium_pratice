import pytest
from LoginPageObject import LoginPage


class TestLogin:
    def test_valid_login(self, setup, base_url):
        driver = setup
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.enter_username("admin")
        login_page.enter_password("admin1234")
        login_page.click_login()
        assert "管理者" == login_page.get_success_user()
        driver.quit()

    def test_invalid_login(self, setup, base_url):
        driver = setup
        driver.get(base_url)
        login_page = LoginPage(driver)
        login_page.enter_username("admin123")
        login_page.enter_password("adm")
        login_page.click_login()
        assert "ErrorCode:[100]:查無使用者資料" == login_page.get_error_message()
        driver.quit()
