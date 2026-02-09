import pytest


class TestDemo4Grouping:

    # 分組執行時，需使用
    # python -m  pytest -v -s -m "group-name" .\pytest_demo\test_4_grouping_demo.py
    # ex:python -m  pytest -v -s -m "sanity" .\pytest_demo\test_4_grouping_demo.py
    # ex:python -m  pytest -v -s -m "sanity and regression" .\pytest_demo\test_4_grouping_demo.py
    # ex:python -m  pytest -v -s -m "sanity not regression" .\pytest_demo\test_4_grouping_demo.py

    @pytest.mark.sanity
    def test_login_by_google(self):
        print("test_test_login_by_google group in sanity")
        assert True

    @pytest.mark.sanity
    def test_login_by_facebook(self):
        print("test_test_login_by_facebook group in sanity")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_by_email(self):
        print("test_test_login_by_email group in sanity and regression")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register(self):
        print("test_test_register group in sanity and regression")
        assert True

    @pytest.mark.sanity
    def test_logout(self):
        print("test_test_logout group in sanity")
        assert True

    @pytest.mark.regression
    def test_order(self):
        print("test_test_order group in regression")
        assert True

    @pytest.mark.regression
    def test_customer_info(self):
        print("test_test_customer_info group in regression")
        assert True
