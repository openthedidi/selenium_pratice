from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://www.dummyticket.com/dummy-ticket-for-visa-application/")


wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)

date_btn = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='departon']")))
date_btn.click()

time.sleep(3)


year_selection = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, '//select[@class="ui-datepicker-year"]')))

option_list_obj = Select(year_selection)
option_list_obj.select_by_visible_text("2027")


month_selection = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, '//select[@class="ui-datepicker-month"]')))

months_option_list_obj = Select(month_selection)
months_option_list_obj.select_by_visible_text("Jan")

date_btns = wait_setting.until(
    EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//a")))

for date_btn in date_btns:
    if date_btn.text == "10":
        date_btn.click()
        break


time.sleep(3)


chrom_drive.quit()
