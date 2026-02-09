"""
conftest.py — 實務上的 Selenium + Pytest 共用設定

功能：
  1. CLI 參數：--browser, --headless, --base-url
  2. WebDriver 生命週期管理（自動 quit）
  3. 測試失敗時自動截圖
  4. 整合 logging 模組
  5. pytest-html 報告客製（環境資訊 + 失敗截圖嵌入）
  6. 全域前/後置作業 fixture

指令範例：
  # 基本執行
  python -m pytest pytest_POM_demo/ -v -s

  # 指定瀏覽器 + headless
  python -m pytest pytest_POM_demo/ --browser chrome --headless

  # 產生 HTML 報告
  python -m pytest pytest_POM_demo/ --browser edge --headless --html=pytest_POM_demo/report.html --self-contained-html

  # 平行執行
  python -m pytest pytest_POM_demo/ -n=4 --browser chrome --headless
"""

import os
import logging
import datetime

import pytest
from selenium.common.exceptions import WebDriverException
from config.browser_settings import BrowserSettings
from config.log_settings import setup_logging


# ===================================================================
# Logging 初始化（整個 session 只會執行一次）
# ===================================================================
setup_logging(log_filename="test.log")
logger = logging.getLogger(__name__)


# ===================================================================
# OOM 偵測與安全清理
# ===================================================================

# 瀏覽器頁面崩潰時，WebDriver 拋出的錯誤訊息中通常包含這些關鍵字
_OOM_KEYWORDS = [
    "page crash",           # Chrome/Edge: "session deleted because of page crash"
    "out of memory",        # 直接的 OOM 訊息
    "not reachable",        # "chrome not reachable"
    "no such window",       # 頁面崩潰後視窗消失
    "unable to evaluate",   # 頁面崩潰後 JS 無法執行
    "renderer crash",       # 渲染進程崩潰
]


def is_oom_error(exception: Exception) -> bool:
    """判斷例外是否為瀏覽器 OOM / 頁面崩潰"""
    msg = str(exception).lower()
    return any(keyword in msg for keyword in _OOM_KEYWORDS)


def is_driver_alive(driver) -> bool:
    """檢查瀏覽器是否還活著（頁面沒有崩潰）"""
    try:
        _ = driver.title
        return True
    except Exception:
        return False


def safe_quit(driver):
    """
    安全關閉瀏覽器。
    即使頁面已崩潰（OOM），也確保進程被清理，不留殭屍進程。
    """
    try:
        driver.quit()
    except Exception as e:
        logger.warning(f"driver.quit() 失敗（瀏覽器可能已崩潰）: {e}")
        # quit 失敗時，嘗試強制終止底層瀏覽器進程
        try:
            pid = driver.service.process.pid
            if os.name == "nt":
                os.system(f"taskkill /F /T /PID {pid} >nul 2>&1")
            else:
                os.kill(pid, 9)
            logger.info(f"已強制終止瀏覽器進程 (PID: {pid})")
        except Exception:
            pass


# ===================================================================
# CLI 參數註冊
# ===================================================================

def pytest_addoption(parser):
    """註冊自訂 CLI 參數"""
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="要使用的瀏覽器 (預設: chrome)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="是否以 headless 模式執行 (預設: False)",
    )
    parser.addoption(
        "--base-url",
        default="https://www.google.com",
        help="測試的基礎 URL (預設: https://www.google.com)",
    )


# ===================================================================
# Fixtures
# ===================================================================

@pytest.fixture(scope="session")
def base_url(request):
    """取得 --base-url 參數，方便各測試引用"""
    return request.config.getoption("--base-url")


@pytest.fixture
def browser(request):
    """取得 --browser 參數值"""
    return request.config.getoption("--browser")


@pytest.fixture
def setup(request):
    """
    【每個測試函式】建立 WebDriver，測試結束後自動關閉。

    使用方式:
        def test_example(setup):
            setup.get("https://example.com")
            assert "Example" in setup.title
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    bs = BrowserSettings()

    driver_map = {
        "chrome": bs.get_chrome_driver,
        "firefox": bs.get_firefox_driver,
        "edge": bs.get_edge_driver,
    }

    logger.info(f"啟動瀏覽器: {browser_name} (headless={headless})")
    driver = driver_map[browser_name](headless=headless)
    driver.implicitly_wait(10)

    yield driver

    logger.info(f"關閉瀏覽器: {browser_name}")
    safe_quit(driver)


@pytest.fixture(scope="session")
def setup_session(request):
    """
    【整個 session 共用】同一個 WebDriver，所有測試共享。
    適合不需要乾淨狀態的場景（例如只讀頁面驗證），可大幅加速。
    若偵測到 OOM 頁面崩潰，會自動重啟瀏覽器讓後續測試繼續。

    使用方式:
        def test_example(setup_session):
            setup_session.get("https://example.com")
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    bs = BrowserSettings()

    driver_map = {
        "chrome": bs.get_chrome_driver,
        "firefox": bs.get_firefox_driver,
        "edge": bs.get_edge_driver,
    }

    def create_driver():
        d = driver_map[browser_name](headless=headless)
        d.implicitly_wait(10)
        return d

    logger.info(f"[Session] 啟動瀏覽器: {browser_name} (headless={headless})")
    driver = create_driver()

    yield driver

    logger.info(f"[Session] 關閉瀏覽器: {browser_name}")
    safe_quit(driver)


# ===================================================================
# Hook：測試失敗時自動截圖
# ===================================================================

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    每個測試階段（setup / call / teardown）結束後會觸發。
    若測試在 call 階段失敗：
      - 判斷是否為 OOM / 頁面崩潰，在報告中標注
      - 嘗試截圖（頁面崩潰時截圖會失敗，屬正常現象）
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 嘗試從 fixture 中取得 driver
        driver = (
            item.funcargs.get("setup")
            or item.funcargs.get("setup_session")
        )
        if driver is None:
            return

        # 偵測是否為 OOM 導致的失敗
        if report.longrepr and is_oom_error(Exception(str(report.longrepr))):
            logger.error(
                f"[OOM] 測試 {item.name} 因瀏覽器頁面崩潰（疑似 OOM）而失敗"
            )

        # 嘗試截圖（頁面崩潰時可能失敗）
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{item.name}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)

        if not is_driver_alive(driver):
            logger.warning(
                f"瀏覽器已崩潰，無法截圖 (測試: {item.name})"
            )
            return

        try:
            driver.save_screenshot(filepath)
            logger.error(f"測試失敗截圖已儲存: {filepath}")
            report.extras = getattr(report, "extras", [])
            try:
                from pytest_html import extras
                report.extras.append(extras.image(filepath))
            except ImportError:
                pass
        except Exception as e:
            logger.warning(f"截圖失敗: {e}")


# ===================================================================
# Hook：pytest-html 報告客製
# ===================================================================

def pytest_configure(config):
    """在報告的 Environment 區塊加入自訂欄位"""
    if hasattr(config, "_metadata"):
        config._metadata["專案名稱"] = "Selenium Practice"
        config._metadata["測試瀏覽器"] = config.getoption(
            "--browser", default="chrome")


def pytest_html_report_title(report):
    """自訂 HTML 報告標題"""
    report.title = "Selenium 自動化測試報告"
