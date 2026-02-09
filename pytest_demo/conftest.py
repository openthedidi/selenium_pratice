import pytest


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
