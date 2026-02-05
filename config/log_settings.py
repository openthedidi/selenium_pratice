"""
Logging 設定模組

提供專案統一的 logging 設定，支援同時輸出到 console 與檔案。
採用 TimedRotatingFileHandler 每日自動輪替，保留 7 天。
搭配自訂 RotatingSizeHandler 限制單日檔案大小，超過時自動編號備份。

使用方式:
    from config.log_settings import setup_logging
    import logging

    # 初始化（整個程式只需呼叫一次）
    setup_logging()

    # 在各模組中取得 logger
    logger = logging.getLogger(__name__)

    logger.debug("除錯訊息，預設不會輸出")
    logger.info("一般流程資訊")
    logger.warning("警告訊息")
    logger.error("錯誤訊息")
    logger.critical("嚴重錯誤")
"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

# 預設 log 檔案存放目錄（專案根目錄下的 logs/）
_DEFAULT_LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# console 格式：簡潔，方便即時查看
_CONSOLE_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

# 檔案格式：詳細，包含檔名與行號，方便事後追查
_FILE_FORMAT = "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d) - %(message)s"

# 時間格式
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
    console_level=logging.INFO,
    file_level=logging.DEBUG,
    log_dir=None,
    log_filename="app.log",
    max_bytes=10 * 1024 * 1024,
    backup_count=7,
):
    """
    初始化專案的 logging 設定。整個程式進入點只需呼叫一次。

    Args:
        console_level: console 輸出的最低等級，預設 INFO
        file_level: 檔案輸出的最低等級，預設 DEBUG（記錄更多細節）
        log_dir: log 檔案存放目錄，預設為專案根目錄下的 logs/
        log_filename: log 檔案名稱，預設 app.log
        max_bytes: 單一 log 檔案大小上限（bytes），預設 10MB，
                   超過時自動編號備份（app.log → app.log.1）
        backup_count: 按日輪替時保留的天數，預設 7 天，
                      超過 7 天的 log 檔案會自動刪除
    """
    if log_dir is None:
        log_dir = _DEFAULT_LOG_DIR

    # 自動建立 log 目錄
    os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, log_filename)

    # 取得 root logger，統一管理所有子 logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # 避免重複初始化（例如被呼叫多次時）
    if root_logger.handlers:
        return

    # --- Console Handler ---
    # 輸出到終端機，顯示簡潔格式
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter(_CONSOLE_FORMAT, _DATE_FORMAT))

    # --- Timed File Handler ---
    # 每日午夜自動輪替（midnight），檔案命名如 app.log.2026-02-05
    # backupCount=7 表示只保留最近 7 天的 log，舊的自動刪除
    timed_handler = TimedRotatingFileHandler(
        log_file_path,
        when="midnight",
        interval=1,
        backupCount=backup_count,
        encoding="utf-8",
    )
    timed_handler.suffix = "%Y-%m-%d"
    timed_handler.setLevel(file_level)
    timed_handler.setFormatter(logging.Formatter(_FILE_FORMAT, _DATE_FORMAT))

    # --- Size File Handler ---
    # 限制單一檔案大小，超過 max_bytes 時自動備份為 app.log.1, app.log.2 ...
    # 保留 3 個備份，避免當天 log 量過大時佔滿硬碟
    size_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=max_bytes,
        backupCount=3,
        encoding="utf-8",
    )
    size_handler.setLevel(file_level)
    size_handler.setFormatter(logging.Formatter(_FILE_FORMAT, _DATE_FORMAT))

    root_logger.addHandler(console_handler)
    root_logger.addHandler(timed_handler)
    root_logger.addHandler(size_handler)
