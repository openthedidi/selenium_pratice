from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.browser_settings import BrowserSettings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import excel_utils
import openpyxl
import os


chrom_drive = BrowserSettings().get_chrome_driver(maximize=True, headless=True)
chrom_drive.get(
    "https://www.skbank.com.tw/carloan_messagebroad")

wait_setting = WebDriverWait(chrom_drive, 10)

# time.sleep(5)


def empty_validate_phone(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='phoneControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位必填']")))
        error_message_list.append("行動電話：此欄位必填")
    except:
        pass


def empty_validate_name(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='nameControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位必填']")))
        error_message_list.append("姓名：此欄位必填")
    except:
        pass


def format_validate_name(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='nameControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位格式錯誤']")))
        error_message_list.append(f"姓名：此欄位格式錯誤")
    except:
        pass


def format_validate_phone(error_message_list, short_wait):
    try:
        short_wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='phoneControl']/ancestor::skbank-input/following-sibling::skbank-error[1]//div[contains(@class,'error__text') and normalize-space()='此欄位格式錯誤']")))
        error_message_list.append(f"行動電話：此欄位格式錯誤")
    except:
        pass


# ---- test data read from excel
excel_file = os.path.join(os.path.dirname(__file__), "test_data", "Test_Case_carloan_messagebroad_final.xlsx")

workbook = openpyxl.load_workbook(excel_file)

rows_number = excel_utils.getRowCount(excel_file, "TestData")

for row in range(5, rows_number + 1):
    error_message_list = []
    chrom_drive.refresh()

    name = excel_utils.readData(excel_file, "TestData", row, 2)
    phone = excel_utils.readData(excel_file, "TestData", row, 3)
    city = excel_utils.readData(excel_file, "TestData", row, 4)
    district = excel_utils.readData(excel_file, "TestData", row, 5)
    bank_branch = excel_utils.readData(excel_file, "TestData", row, 6)
    print(name, phone, city, district, bank_branch)

    name_input = wait_setting.until(EC.visibility_of_element_located(
        (By.ID, "nameControl")))
    name_input.send_keys(name)

    phone_input = wait_setting.until(EC.visibility_of_element_located(
        (By.ID, "phoneControl")))
    phone_input.send_keys(str(phone))

    # 檢查 name 的驗證
    short_wait = WebDriverWait(chrom_drive, 1)
    empty_validate_name(error_message_list, short_wait)
    format_validate_name(error_message_list, short_wait)

    # 檢查 phone 的驗證
    empty_validate_phone(error_message_list, short_wait)
    format_validate_phone(error_message_list, short_wait)

    city_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='指定分行縣市']")))

    chrom_drive.execute_script("arguments[0].click();", city_select)

    city_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, f"//span[text()='{city}']")))

    chrom_drive.execute_script("arguments[0].click();", city_span)

    district_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='指定分行鄉鎮市區']")))

    chrom_drive.execute_script("arguments[0].click();", district_select)

    district_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, f"//span[text()='{district}']")))

    chrom_drive.execute_script("arguments[0].click();", district_span)

    bank_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='選擇分行']")))

    chrom_drive.execute_script("arguments[0].click();", bank_select)

    bank_branch_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, f"//span[text()='{bank_branch}']")))

    chrom_drive.execute_script("arguments[0].click();", bank_branch_span)

    privacy_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='consulation-request__block']//div[@class='checkbox__icon-box']")))

    chrom_drive.execute_script("arguments[0].click();", privacy_span)
    print(error_message_list)
    if error_message_list:
        for error_message in error_message_list:
            excel_utils.fillRedColor(excel_file, "TestData", row, 8)
            excel_utils.writeData(excel_file, "TestData",
                                  row, 8, error_message)
    else:
        excel_utils.fillGreenColor(excel_file, "TestData", row, 8)
        excel_utils.writeData(excel_file, "TestData", row, 8, "pass")


input("123")
chrom_drive.quit()
