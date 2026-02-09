import pytest


class TestDemo:

    @pytest.fixture
    def setup(self):
        print("測試前，執行前置作業邏輯，如開啟config")
        yield
        print("測試結束，執行後置作業邏輯")

    def test_demo1(self, setup, configSetting4Gobal):
        print("test test_demo1 with setup")
        assert True

    def test_demo2(self, configSetting4GobalInOption):
        print("test test_demo2 without setup")
        assert True

    def test_demo3(self, setup):
        print("test test_demo3 without setup")
        assert False
