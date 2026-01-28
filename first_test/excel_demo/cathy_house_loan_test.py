from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
from first_test.excel_demo import excel_utils


chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-monthly-payments/")

chrom_drive.maximize_window()
wait_setting = WebDriverWait(chrom_drive, 3)


# ---- test data read from excel
excel_file = "D:\\selenium-driver\\ClassExamples\\ClassExamples\\caldata.xlsx"

workbook = openpyxl.load_workbook(excel_file)
sheet = workbook["Sheet2"]

excel_utils.getColumnCount(excel_file, "Sheet2")
excel_utils.getRowCount(excel_file, "Sheet2")


title_data = excel_utils.readRow(excel_file, "Sheet2", 1)

row1_data = excel_utils.readRow(excel_file, "Sheet2", 2)

row2_data = excel_utils.readRow(excel_file, "Sheet2", 3)


# 用dict , title is key and row-data is value

row1_data_dict = {}
for i in range(len(title_data)):
    row1_data_dict[title_data[i]] = row1_data[i]

row2_data_dict = {}
for i in range(len(title_data)):
    row2_data_dict[title_data[i]] = row2_data[i]

total_test_data = []
total_test_data.append(row1_data_dict)
total_test_data.append(row2_data_dict)

row = 2


for test_datas in total_test_data:

    loan_amount_input = wait_setting.until(
        EC.presence_of_element_located((By.ID, "amount")))
    loan_amount_input.clear()
    loan_amount_input.send_keys(test_datas['貸款金額'])

    loan_20year_radio_label = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='tab1']")))
    loan_30year_radio_label = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='tab2']")))
    if test_datas['貸款年限'] == 20:
        chrom_drive.execute_script(
            "arguments[0].click();", loan_20year_radio_label)
    else:
        chrom_drive.execute_script(
            "arguments[0].click();", loan_30year_radio_label)

    fee = wait_setting.until(
        EC.presence_of_element_located((By.NAME, "Fee")))
    fee.clear()
    fee.send_keys(test_datas['相關費用'])

    extensionY = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='extensionY']")))
    extensionY.clear()
    extensionY.send_keys(test_datas['寬限期'])

    pay_way_radio_label = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='customPayFor1']")))
    chrom_drive.execute_script(
        "arguments[0].click();", pay_way_radio_label)

    rat_label = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//label[@for='tab-list-1']")))
    chrom_drive.execute_script("arguments[0].click();", rat_label)

    period2_input = wait_setting.until(
        EC.presence_of_element_located((By.ID, "period11")))
    period2_input.clear()
    period2_input.send_keys(test_datas['最終月'])

    periodrate1_input = wait_setting.until(
        EC.presence_of_element_located((By.ID, "periodrate1")))
    periodrate1_input.clear()
    periodrate1_input.send_keys(test_datas['利率'])

    start_btn = wait_setting.until(
        EC.presence_of_element_located((By.ID, "formSubmitBtn")))

    chrom_drive.execute_script("arguments[0].click();", start_btn)

    result_span_list = wait_setting.until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[@class='cubinvest-highlight']")))

    expected_1 = test_datas['第1 ~ 36個月預期']
    expected_2 = test_datas['第37 ~ 239個月預期']
    expected_3 = test_datas['第240個月預期']

    actual_1 = result_span_list[0].text
    actual_2 = result_span_list[1].text
    actual_3 = result_span_list[2].text

    print(f"第1~36 預期:{expected_1} 實際:{actual_1}")
    print(f"第37~239 預期:{expected_2} 實際:{actual_2}")
    print(f"第240 預期:{expected_3} 實際:{actual_3}")

    errors = []
    if actual_1 != expected_1:
        errors.append(f"第1~36 預期:{expected_1} 實際:{actual_1}")
    if actual_2 != expected_2:
        errors.append(f"第37~239 預期:{expected_2} 實際:{actual_2}")
    if actual_3 != expected_3:
        errors.append(f"第240 預期:{expected_3} 實際:{actual_3}")

    if errors:
        excel_utils.writeData(excel_file, "Sheet2", row,
                              13, " ; ".join(errors))
        excel_utils.fillRedColor(excel_file, "Sheet2", row, 13)
    else:
        excel_utils.writeData(excel_file, "Sheet2", row, 13, "OK")
        excel_utils.fillGreenColor(excel_file, "Sheet2", row, 13)
    row += 1


workbook.close()
chrom_drive.quit()
