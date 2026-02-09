from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.browser_settings import BrowserSettings
from config.log_settings import setup_logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import excel_utils
from utils.exceptions import ExcelFileNotFoundError, ExcelSheetNotFoundError, ExcelDataError
import openpyxl
import os
import logging

# 啟動 log紀錄
setup_logging(file_level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("啟動chrome瀏覽器")
driver = BrowserSettings().get_chrome_driver(maximize=True, headless=True)
driver.get(
    "https://www.skbank.com.tw/carloan_messagebroad")
logger.info("開啟：https://www.skbank.com.tw/carloan_messagebroad")

wait_setting = WebDriverWait(driver, 10)


def empty_validate_phone(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='phoneControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位必填']")))
        error_message_list.append("行動電話：此欄位必填")
        logger.warning("行動電話：此欄位必填")
    except:
        pass


def empty_validate_name(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='nameControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位必填']")))
        error_message_list.append("姓名：此欄位必填")
        logger.warning("姓名：此欄位必填")
    except:
        pass


def format_validate_name(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='nameControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位格式錯誤']")))
        error_message_list.append(f"姓名：此欄位格式錯誤")
        logger.warning("姓名：此欄位格式錯誤")
    except:
        pass


def format_validate_phone(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='phoneControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位格式錯誤']")))
        error_message_list.append(f"行動電話：此欄位格式錯誤")
        logger.warning("行動電話：此欄位格式錯誤")
    except:
        pass


# ---- test data read from excel
excel_file = os.path.join(os.path.dirname(
    __file__), "test_data", "Test_Case_carloan_messagebroad_final.xlsx")

# 檢查 Excel 檔案是否存在
if not os.path.exists(excel_file):
    logger.error("找不到測試資料: %s", excel_file)
    raise ExcelFileNotFoundError(excel_file)

logger.info("讀取測試資料: %s", excel_file)
workbook = openpyxl.load_workbook(excel_file)

# 檢查工作表是否存在
sheet_name = "TestData"
if sheet_name not in workbook.sheetnames:
    logger.error("找不到工作表: %s", sheet_name)
    raise ExcelSheetNotFoundError(excel_file, sheet_name)

rows_number = excel_utils.get_row_count(excel_file, sheet_name)
logger.info("共 %d 筆測試資料（從第 5 列開始）", rows_number - 4)

for row in range(5, rows_number + 1):
    error_message_list = []
    driver.refresh()

    try:
        name = excel_utils.read_data(excel_file, sheet_name, row, 2)
        phone = excel_utils.read_data(excel_file, sheet_name, row, 3)
        city = excel_utils.read_data(excel_file, sheet_name, row, 4)
        district = excel_utils.read_data(excel_file, sheet_name, row, 5)
        bank_branch = excel_utils.read_data(excel_file, sheet_name, row, 6)

        # 檢查必要欄位是否有值，有空值則拋出 ExcelDataError
        required_fields = {"name": name, "phone": phone, "city": city,
                           "district": district, "bank_branch": bank_branch}
        for col_idx, (field_name, value) in enumerate(required_fields.items(), start=2):
            if value is None:
                raise ExcelDataError(excel_file, sheet_name, row, col_idx,
                                     f"{field_name} 欄位值為空")

        logger.info("=== 第 %d 列 | name=%s, phone=%s, city=%s, district=%s, branch=%s ===",
                    row, name, phone, city, district, bank_branch)

        name_input = wait_setting.until(EC.visibility_of_element_located(
            (By.ID, "nameControl")))
        name_input.send_keys(name)

        phone_input = wait_setting.until(EC.visibility_of_element_located(
            (By.ID, "phoneControl")))
        phone_input.send_keys(str(phone))

        # 檢查 name 的驗證
        short_wait = WebDriverWait(driver, 0.5)
        empty_validate_name(error_message_list, short_wait)
        format_validate_name(error_message_list, short_wait)

        # 檢查 phone 的驗證
        empty_validate_phone(error_message_list, short_wait)
        format_validate_phone(error_message_list, short_wait)

        city_select = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='指定分行縣市']")))

        driver.execute_script("arguments[0].click();", city_select)

        city_span = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, f"//span[text()='{city}']")))

        driver.execute_script("arguments[0].click();", city_span)

        district_select = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='指定分行鄉鎮市區']")))

        driver.execute_script("arguments[0].click();", district_select)

        district_span = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, f"//span[text()='{district}']")))

        driver.execute_script("arguments[0].click();", district_span)

        bank_select = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='選擇分行']")))

        driver.execute_script("arguments[0].click();", bank_select)

        bank_branch_span = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, f"//span[text()='{bank_branch}']")))

        driver.execute_script("arguments[0].click();", bank_branch_span)

        privacy_span = wait_setting.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='consulation-request__block']//div[@class='checkbox__icon-box']")))

        driver.execute_script("arguments[0].click();", privacy_span)

    except Exception as e:
        # 捕捉所有例外（含 ExcelDataError、Selenium TimeoutException 等）
        error_message_list.append(str(e))
        logger.error("第 %d 列執行異常: %s", row, e)

    if error_message_list:
        excel_utils.fill_red_color(excel_file, sheet_name, row, 8)
        excel_utils.write_data(excel_file, sheet_name,
                              row, 8, "；".join(error_message_list))
        logger.error("第 %d 列Nagetive測試: %s", row, "；".join(error_message_list))
    else:
        excel_utils.fill_green_color(excel_file, sheet_name, row, 8)
        excel_utils.write_data(excel_file, sheet_name, row, 8, "pass")
        logger.info("第 %d 列Positive測試: pass", row)

logger.info("所有測試執行完畢，關閉瀏覽器")
driver.quit()
