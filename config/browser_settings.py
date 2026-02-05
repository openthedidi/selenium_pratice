"""
瀏覽器設定模組

提供統一的瀏覽器設定介面，支援 Chrome、Edge、Firefox 三種瀏覽器。
包含常用的自動化測試設定選項。
"""

from selenium import webdriver


class BrowserSettings:
    """
    統一的瀏覽器設定模組，支援 Chrome、Edge、Firefox 三種瀏覽器。

    使用範例:
        browser = BrowserSettings()

        # 基本使用
        driver = browser.get_chrome_driver()

        # 啟用 headless 模式
        driver = browser.get_chrome_driver(headless=True)

        # 指定下載目錄
        driver = browser.get_edge_driver(download_dir="D:/downloads")

        # 完整設定
        driver = browser.get_chrome_driver(
            download_dir="D:/downloads",
            headless=True,
            disable_gpu=True,
            window_size=(1920, 1080),
            disable_images=True,
            incognito=True
        )
    """

    # =========================================================================
    # 公開方法 - 取得 WebDriver
    # =========================================================================

    def get_chrome_driver(
        self,
        download_dir: str = None,
        headless: bool = False,
        disable_gpu: bool = False,
        maximize: bool = False,
        window_size: tuple = None,
        disable_images: bool = False,
        ignore_ssl_errors: bool = False,
        disable_automation: bool = False,
        detach: bool = False,
        incognito: bool = False,
        user_agent: str = None,
        disable_extensions: bool = False,
        disable_popup_blocking: bool = False,
    ):
        """
        建立並返回 Chrome WebDriver。

        Args:
            download_dir (str): 下載目錄路徑，None 則使用預設
            headless (bool): 無頭模式，不顯示瀏覽器視窗
            disable_gpu (bool): 禁用 GPU 加速，headless 模式建議開啟
            maximize (bool): 啟動時最大化視窗
            window_size (tuple): 視窗大小，格式 (寬, 高)，如 (1920, 1080)
            disable_images (bool): 禁用圖片載入，可加速測試
            ignore_ssl_errors (bool): 忽略 SSL 憑證錯誤
            disable_automation (bool): 隱藏自動化控制提示，降低被偵測機率
            detach (bool): 執行完畢後保持瀏覽器開啟，方便除錯
            incognito (bool): 無痕模式
            user_agent (str): 自訂 User-Agent 字串
            disable_extensions (bool): 禁用所有擴充功能
            disable_popup_blocking (bool): 禁用彈出視窗封鎖

        Returns:
            webdriver.Chrome: Chrome WebDriver 實例
        """
        ops = self._get_chrome_options(
            download_dir=download_dir,
            headless=headless,
            disable_gpu=disable_gpu,
            maximize=maximize,
            window_size=window_size,
            disable_images=disable_images,
            ignore_ssl_errors=ignore_ssl_errors,
            disable_automation=disable_automation,
            detach=detach,
            incognito=incognito,
            user_agent=user_agent,
            disable_extensions=disable_extensions,
            disable_popup_blocking=disable_popup_blocking,
        )
        return webdriver.Chrome(options=ops)

    def get_edge_driver(
        self,
        download_dir: str = None,
        headless: bool = False,
        disable_gpu: bool = False,
        maximize: bool = False,
        window_size: tuple = None,
        disable_images: bool = False,
        ignore_ssl_errors: bool = False,
        disable_automation: bool = False,
        detach: bool = False,
        inprivate: bool = False,
        user_agent: str = None,
        disable_extensions: bool = False,
        disable_popup_blocking: bool = False,
    ):
        """
        建立並返回 Edge WebDriver。

        Args:
            download_dir (str): 下載目錄路徑，None 則使用預設
            headless (bool): 無頭模式，不顯示瀏覽器視窗
            disable_gpu (bool): 禁用 GPU 加速，headless 模式建議開啟
            maximize (bool): 啟動時最大化視窗
            window_size (tuple): 視窗大小，格式 (寬, 高)，如 (1920, 1080)
            disable_images (bool): 禁用圖片載入，可加速測試
            ignore_ssl_errors (bool): 忽略 SSL 憑證錯誤
            disable_automation (bool): 隱藏自動化控制提示，降低被偵測機率
            detach (bool): 執行完畢後保持瀏覽器開啟，方便除錯
            inprivate (bool): InPrivate 隱私模式
            user_agent (str): 自訂 User-Agent 字串
            disable_extensions (bool): 禁用所有擴充功能
            disable_popup_blocking (bool): 禁用彈出視窗封鎖

        Returns:
            webdriver.Edge: Edge WebDriver 實例
        """
        ops = self._get_edge_options(
            download_dir=download_dir,
            headless=headless,
            disable_gpu=disable_gpu,
            maximize=maximize,
            window_size=window_size,
            disable_images=disable_images,
            ignore_ssl_errors=ignore_ssl_errors,
            disable_automation=disable_automation,
            detach=detach,
            inprivate=inprivate,
            user_agent=user_agent,
            disable_extensions=disable_extensions,
            disable_popup_blocking=disable_popup_blocking,
        )
        return webdriver.Edge(options=ops)

    def get_firefox_driver(
        self,
        download_dir: str = None,
        headless: bool = False,
        disable_gpu: bool = False,
        maximize: bool = False,
        window_size: tuple = None,
        disable_images: bool = False,
        ignore_ssl_errors: bool = False,
        private: bool = False,
        user_agent: str = None,
    ):
        """
        建立並返回 Firefox WebDriver。

        Args:
            download_dir (str): 下載目錄路徑，None 則使用預設
            headless (bool): 無頭模式，不顯示瀏覽器視窗
            disable_gpu (bool): 禁用 GPU 加速
            maximize (bool): 啟動時最大化視窗（Firefox 需在啟動後呼叫）
            window_size (tuple): 視窗大小，格式 (寬, 高)，如 (1920, 1080)
            disable_images (bool): 禁用圖片載入，可加速測試
            ignore_ssl_errors (bool): 忽略 SSL 憑證錯誤
            private (bool): 隱私瀏覽模式
            user_agent (str): 自訂 User-Agent 字串

        Returns:
            webdriver.Firefox: Firefox WebDriver 實例
        """
        ops = self._get_firefox_options(
            download_dir=download_dir,
            headless=headless,
            disable_gpu=disable_gpu,
            window_size=window_size,
            disable_images=disable_images,
            ignore_ssl_errors=ignore_ssl_errors,
            private=private,
            user_agent=user_agent,
        )
        driver = webdriver.Firefox(options=ops)

        # Firefox 的最大化需要在啟動後執行
        if maximize:
            driver.maximize_window()

        return driver

    # =========================================================================
    # 內部方法 - 建立 Options 物件
    # =========================================================================

    def _get_chrome_options(
        self,
        download_dir=None,
        headless=False,
        disable_gpu=False,
        maximize=False,
        window_size=None,
        disable_images=False,
        ignore_ssl_errors=False,
        disable_automation=False,
        detach=False,
        incognito=False,
        user_agent=None,
        disable_extensions=False,
        disable_popup_blocking=False,
    ):
        """
        設定並返回 ChromeOptions 物件。

        Returns:
            webdriver.ChromeOptions: 設定完成的 ChromeOptions
        """
        ops = webdriver.ChromeOptions()

        # ----- 基本偏好設定 -----
        prefs = {
            # 下載設定：不詢問下載位置，自動下載
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            # 安全瀏覽：保持啟用以避免惡意檔案
            "safebrowsing.enabled": True,
            # PDF：直接下載而非在瀏覽器中開啟
            "plugins.always_open_pdf_externally": True,
            # 通知：2 = 封鎖所有網站通知
            "profile.default_content_setting_values.notifications": 2,
            # 語系：優先使用繁體中文
            "intl.accept_languages": "zh-TW,zh,en-US,en",
        }

        # 設定下載目錄
        if download_dir:
            prefs["download.default_directory"] = download_dir

        # 禁用圖片載入（加速頁面載入）
        # 1 = 允許, 2 = 封鎖
        if disable_images:
            prefs["profile.managed_default_content_settings.images"] = 2

        ops.add_experimental_option("prefs", prefs)

        # ----- 命令列參數 -----

        # 無頭模式：不顯示瀏覽器視窗，適合 CI/CD 環境
        if headless:
            ops.add_argument("--headless=new")

        # 禁用 GPU：在無頭模式或某些環境下可避免錯誤
        if disable_gpu:
            ops.add_argument("--disable-gpu")

        # 啟動時最大化視窗
        if maximize:
            ops.add_argument("--start-maximized")

        # 設定視窗大小，格式：寬,高
        if window_size:
            ops.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

        # 忽略 SSL 憑證錯誤（測試環境使用自簽憑證時）
        if ignore_ssl_errors:
            ops.add_argument("--ignore-certificate-errors")
            ops.add_argument("--ignore-ssl-errors")

        # 無痕模式
        if incognito:
            ops.add_argument("--incognito")

        # 自訂 User-Agent
        if user_agent:
            ops.add_argument(f"--user-agent={user_agent}")

        # 禁用擴充功能
        if disable_extensions:
            ops.add_argument("--disable-extensions")

        # 禁用彈出視窗封鎖
        if disable_popup_blocking:
            ops.add_argument("--disable-popup-blocking")

        # ----- 實驗性選項 -----

        # 隱藏自動化控制提示：移除 "Chrome is being controlled by automated software" 提示
        if disable_automation:
            ops.add_experimental_option("excludeSwitches", ["enable-automation"])
            ops.add_experimental_option("useAutomationExtension", False)

        # Detach 模式：腳本結束後保持瀏覽器開啟，方便除錯
        if detach:
            ops.add_experimental_option("detach", True)

        return ops

    def _get_edge_options(
        self,
        download_dir=None,
        headless=False,
        disable_gpu=False,
        maximize=False,
        window_size=None,
        disable_images=False,
        ignore_ssl_errors=False,
        disable_automation=False,
        detach=False,
        inprivate=False,
        user_agent=None,
        disable_extensions=False,
        disable_popup_blocking=False,
    ):
        """
        設定並返回 EdgeOptions 物件。
        Edge 基於 Chromium，大部分設定與 Chrome 相同。

        Returns:
            webdriver.EdgeOptions: 設定完成的 EdgeOptions
        """
        ops = webdriver.EdgeOptions()

        # ----- 基本偏好設定（與 Chrome 相同） -----
        prefs = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_setting_values.notifications": 2,
            "intl.accept_languages": "zh-TW,zh,en-US,en",
        }

        if download_dir:
            prefs["download.default_directory"] = download_dir

        if disable_images:
            prefs["profile.managed_default_content_settings.images"] = 2

        ops.add_experimental_option("prefs", prefs)

        # ----- 命令列參數 -----

        if headless:
            ops.add_argument("--headless=new")

        if disable_gpu:
            ops.add_argument("--disable-gpu")

        if maximize:
            ops.add_argument("--start-maximized")

        if window_size:
            ops.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

        if ignore_ssl_errors:
            ops.add_argument("--ignore-certificate-errors")
            ops.add_argument("--ignore-ssl-errors")

        # Edge 使用 inprivate 而非 incognito
        if inprivate:
            ops.add_argument("--inprivate")

        if user_agent:
            ops.add_argument(f"--user-agent={user_agent}")

        if disable_extensions:
            ops.add_argument("--disable-extensions")

        if disable_popup_blocking:
            ops.add_argument("--disable-popup-blocking")

        # ----- 實驗性選項 -----

        if disable_automation:
            ops.add_experimental_option("excludeSwitches", ["enable-automation"])
            ops.add_experimental_option("useAutomationExtension", False)

        if detach:
            ops.add_experimental_option("detach", True)

        return ops

    def _get_firefox_options(
        self,
        download_dir=None,
        headless=False,
        disable_gpu=False,
        window_size=None,
        disable_images=False,
        ignore_ssl_errors=False,
        private=False,
        user_agent=None,
    ):
        """
        設定並返回 FirefoxOptions 物件。
        Firefox 使用 set_preference() 而非 prefs 字典。

        Returns:
            webdriver.FirefoxOptions: 設定完成的 FirefoxOptions
        """
        ops = webdriver.FirefoxOptions()

        # ----- 下載設定 -----
        # folderList: 0=桌面, 1=下載資料夾, 2=自訂位置
        ops.set_preference("browser.download.folderList", 2)
        # 下載時不顯示下載管理員
        ops.set_preference("browser.download.manager.showWhenStarting", False)
        # 不詢問即下載的 MIME 類型
        ops.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/pdf,application/octet-stream,application/zip,"
            "application/x-zip-compressed,application/vnd.ms-excel,"
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,"
            "text/csv,text/plain"
        )
        # 禁用內建 PDF 檢視器，直接下載 PDF
        ops.set_preference("pdfjs.disabled", True)

        # ----- 語系設定 -----
        ops.set_preference("intl.accept_languages", "zh-TW,zh,en-US,en")

        # ----- 下載目錄 -----
        if download_dir:
            ops.set_preference("browser.download.dir", download_dir)

        # ----- 命令列參數 -----

        # 無頭模式
        if headless:
            ops.add_argument("--headless")

        # 禁用 GPU
        if disable_gpu:
            ops.set_preference("layers.acceleration.disabled", True)

        # 視窗大小
        if window_size:
            ops.add_argument(f"--width={window_size[0]}")
            ops.add_argument(f"--height={window_size[1]}")

        # ----- 偏好設定 -----

        # 禁用圖片載入
        # permissions.default.image: 1=允許, 2=封鎖
        if disable_images:
            ops.set_preference("permissions.default.image", 2)

        # 忽略 SSL 憑證錯誤
        if ignore_ssl_errors:
            ops.set_preference("webdriver_accept_untrusted_certs", True)
            ops.set_preference("webdriver_assume_untrusted_issuer", True)

        # 隱私瀏覽模式
        if private:
            ops.add_argument("-private")

        # 自訂 User-Agent
        if user_agent:
            ops.set_preference("general.useragent.override", user_agent)

        return ops
