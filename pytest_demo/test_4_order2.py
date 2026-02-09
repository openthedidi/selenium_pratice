import pytest


class Test4Order:

    # 需要安裝pytest-ordering package
    @pytest.mark.run(order=3)
    def test_order_3(self):
        print("test_order_3")

    @pytest.mark.run(order=2)
    def test_order_2(self):
        print("test_order_2")

    @pytest.mark.run(order=1)
    def test_order_1(self):
        print("test_order_1")
