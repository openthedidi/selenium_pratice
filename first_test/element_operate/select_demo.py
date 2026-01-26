import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://tiponet.tipo.gov.tw/020_OUT_V1/registry.do")
chrom_drive.maximize_window()

wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)

# -------方法1：引入 Select類，執行點選選項的動作
select_btn = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, "//select[@name='stLocalAddr_1']")))


option_list_obj = Select(select_btn)

# for option in option_list_obj.options:
#     print(option.text)


# option_list_obj.select_by_visible_text("基隆市")
# option_list.select_by_value("1")
# option_list.select_by_index(1)


# -------方法2：直接找option
option_btn = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, "//select[@id='stLocalAddr_1']//option[text()='台北市']")))

option_btn.click()


input("Press Enter to close the browser...")
chrom_drive.quit()
