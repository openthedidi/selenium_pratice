from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://jqueryui.com/datepicker/")
chrom_drive.maximize_window()


wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)

# switch to frame

iframe = wait_setting.until(
    EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']")))

chrom_drive.switch_to.frame(iframe)


# date picker from jqury

date_picker = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='datepicker']")))


date_picker.click()

# ------直接輸入
# date_picker.send_keys("11/31/2023")

# ------選擇日期
target_year = '2024'
target_month = 'July'
target_day = '20'

default_month_list = ['January', 'February', 'March', 'April', 'May',
                      'June', 'July', 'August', 'September', 'October', 'November', 'December']


time.sleep(1)

# ---------坑點:如果此類元素有需要重複操作者，都需要重新再找元素，不然會遇到StaleElementReferenceException
while True:
    year_title = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-year']")))
    month_title = wait_setting.until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-month']")))
    next_btn = chrom_drive.find_element(By.XPATH, "//span[text()='Next']")
    prev_btn = chrom_drive.find_element(By.XPATH, "//span[text()='Prev']")

    current_year = int(year_title.text)
    target_year_int = int(target_year)

    current_month_idx = default_month_list.index(month_title.text)
    target_month_idx = default_month_list.index(target_month)

    if current_year < target_year_int:
        next_btn.click()
    elif current_year > target_year_int:
        prev_btn.click()
    else:
        if current_month_idx < target_month_idx:
            next_btn.click()
        elif current_month_idx > target_month_idx:
            prev_btn.click()
        else:
            break


date_table_btns = wait_setting.until(
    EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//a")))

for date_btn in date_table_btns:
    if date_btn.text == target_day:
        date_btn.click()
        break


time.sleep(3)


chrom_drive.quit()
