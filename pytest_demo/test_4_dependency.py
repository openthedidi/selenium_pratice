import pytest


class Test4DependencyDemo:

    # 需要安裝pytest-dependency

    @pytest.mark.dependency()
    def test_home_page(self):
        print("test home_page")
        assert True

    @pytest.mark.dependency()
    def test_login_page(self):
        print("test login_page")
        assert False

    @pytest.mark.dependency(depends=["Test4DependencyDemo::test_home_page", "Test4DependencyDemo::test_login_page"])
    def test_order_page(self):
        print("test order_page")

    @pytest.mark.dependency(depends=["Test4DependencyDemo::test_login_page"])
    def test_customer_info_page(self):
        print("test customer_info_page")
