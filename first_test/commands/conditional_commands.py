from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://demo.nopcommerce.com/register")


chrom_drive.maximize_window()

# ------- is_displayed() & is_enabled() -------

input_search = chrom_drive.find_element(
    By.XPATH, "//input[@id='small-searchterms']")
print(input_search.is_displayed())
print(input_search.is_enabled())

# is_displayed() 檢查元素是否在頁面上可見 (沒有被隱藏)
print(f"搜尋框是否可見? {input_search.is_displayed()}")  # 預期: True

# -------is_enabled
print(f"搜尋框是否可使用? {input_search.is_enabled()}")  # 預期: True

# ------is_selected：只適用在checkBox、radio btn、下拉選單中的option
radio_female = chrom_drive.find_element(
    By.XPATH, "//input[@id='gender-female']")
print(radio_female.is_selected())  # 預期: False

radio_female.click()
print(radio_female.is_selected())  # 預期: True
chrom_drive.quit()


#

nanshan_life = webdriver.Chrome()
nanshan_life.get("https://www.nanshanlife.com.tw/nanshanlife/products-health")
nanshan_life.maximize_window()

time.sleep(5)
search_btn = nanshan_life.find_element(
    By.XPATH, "//nanshan-input-search-bar[@class='ng-untouched ng-valid ng-dirty']//nxtle-icon[@icon='search']//*[name()='svg']")
print(search_btn.is_displayed())
print(search_btn.is_enabled())
print(search_btn.is_selected())


search_input = nanshan_life.find_element(
    By.ID, "search")
print(search_input.is_enabled)
search_input.send_keys("20")
print("-----after input-----")
print(search_btn.is_enabled())
