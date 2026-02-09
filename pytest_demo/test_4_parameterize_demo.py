import pytest


class TestDemo4Parameterize:

    @pytest.mark.parametrize("number1,number2", [(20, 20), (40, 50), (60, 20), ("李四", 25), ("王五", 30)])
    def test_demo1(self, number1, number2):

        assert number1 == number2
