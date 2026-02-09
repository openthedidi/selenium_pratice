from selenium import webdriver
import os


class ChromeSettings:
    def __init__(self):
        pass

    def get_chrome_driver(self, download_dir=None, headless=False):
        ops = self.get_chrome_options(download_dir)
        if headless:
            ops.add_argument("--headless")
        return webdriver.Chrome(options=ops)

    def get_chrome_options(self, download_dir):
        """
        設定並返回 ChromeOptions 物件。
        """
        ops = webdriver.ChromeOptions()
        # # 1) 常用：少一些 automation 提示
        # ops.add_experimental_option("excludeSwitches", ["enable-automation"])
        # ops.add_experimental_option("useAutomationExtension", False)

        # # 2) Debug：跑完不關
        # ops.add_experimental_option("detach", True)

        # # 3) 下載/通知/語系
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_setting_values.notifications": 2,
            "intl.accept_languages": "zh-TW,zh,en-US,en",
        }
        ops.add_experimental_option("prefs", prefs)

        return ops
