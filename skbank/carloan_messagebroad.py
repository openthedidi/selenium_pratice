from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.browser_settings import BrowserSettings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import excel_utils
import openpyxl


chrom_drive = BrowserSettings().get_chrome_driver(maximize=True)
chrom_drive.get(
    "https://www.skbank.com.tw/carloan_messagebroad")

wait_setting = WebDriverWait(chrom_drive, 10)

# time.sleep(5)


# ---- test data read from excel
excel_file = "D:\\QA\\skbank\\Test_Case_carloan_messagebroad_final.xlsx"

workbook = openpyxl.load_workbook(excel_file)
test_Data_sheet = workbook["TestData"]

rows_number = excel_utils.getRowCount(excel_file, "TestData")

for row in range(5, rows_number + 1):
    error_message = ""

    name = excel_utils.readData(excel_file, "TestData", row, 1)
    phone = excel_utils.readData(excel_file, "TestData", row, 2)
    city = excel_utils.readData(excel_file, "TestData", row, 3)
    district = excel_utils.readData(excel_file, "TestData", row, 4)
    bank_branch = excel_utils.readData(excel_file, "TestData", row, 5)
    print(name, phone, city, district, bank_branch)

    name_input = wait_setting.until(EC.visibility_of_element_located(
        (By.ID, "nameControl")))
    name_input.send_keys("Tom")

    is_blank_name_input = EC.visibility_of_element_located(
        (By.ID, "//div[@class='form-field__field']//div[contains(.,'此欄位必填') and @class='h27 error__text']"))

    is_invaild_name_input = EC.visibility_of_element_located(
        (By.ID, "//div[@class='form-field__field']//div[contains(.,'此欄位格式錯誤') and @class='h27 error__text']"))

    phone_input = wait_setting.until(EC.visibility_of_element_located(
        (By.ID, "phoneControl")))

    phone_input.send_keys("09123")

    city_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='指定分行縣市']")))

    chrom_drive.execute_script("arguments[0].click();", city_select)

    city_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='台北市']")))

    chrom_drive.execute_script("arguments[0].click();", city_span)

    district_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='指定分行鄉鎮市區']")))

    chrom_drive.execute_script("arguments[0].click();", district_select)

    district_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='中正區']")))

    chrom_drive.execute_script("arguments[0].click();", district_span)

    babk_select = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='選擇分行']")))

    chrom_drive.execute_script("arguments[0].click();", babk_select)

    bank_branch_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='中正分行']")))

    chrom_drive.execute_script("arguments[0].click();", bank_branch_span)

    privacy_span = wait_setting.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='consulation-request__block']//div[@class='checkbox__icon-box']")))

    chrom_drive.execute_script("arguments[0].click();", privacy_span)


input("123")
chrom_drive.quit()
