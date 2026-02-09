import pytest


class Test4Order:

    # 需要安裝pytest-ordering package，並使用pytest.ini檔

    @pytest.mark.second
    def test_order_2(self):
        print("test_order_2")

    @pytest.mark.first
    def test_order_1(self):
        print("test_order_1")
