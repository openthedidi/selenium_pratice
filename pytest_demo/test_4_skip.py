import pytest
import sys


class TestDemoSkip:

    def test_skip_demo1(self):
        print("test_skip_demo1")

    @pytest.mark.skip(reason="本次不執行")
    def test_skip_demo2(self):
        print("test_skip_demo2")

    @pytest.mark.skipif(sys.platform != "win32", reason="只有在windows才執行")
    def test_skip_demo3(self):
        print("test_skip_demo3，只有在windows才執行")
