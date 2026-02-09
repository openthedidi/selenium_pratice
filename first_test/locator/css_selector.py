# locator分成兩種：
# 1. html檔案上面的屬性 (Attribute) 定位：(通常可以一眼就看出來)
#    - ID: 使用元素的 id 屬性，通常是唯一且最快的定位方式。
#    - Name: 使用元素的 name 屬性，常用於表單元素。
#    - Class Name: 使用元素的 class 屬性。
#    - Tag Name: 使用 HTML 標籤名稱 (例如 'div', 'a', 'input')。
#    - Link Text: 專門用於定位 <a> 標籤，使用完整的連結文字。
#    - Partial Link Text: 專門用於定位 <a> 標籤，使用部分的連結文字。

# 2. 結構/路徑 (Structure/Path) 定位：
#    - XPath: 使用 XML 路徑語言來撈全部的 HTML DOM 結構，功能強大但語法較複雜，速度相對較慢。
#    - CSS Selector: 使用 CSS 選擇器語法來定位元素，語法比 XPath 簡潔，執行速度通常比 XPath快，方式透過tag、name、attribute等等組合來過濾所需的元素。

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get(
    "https://demo.nopcommerce.com/")
driver.maximize_window()

time.sleep(1)

# =============css selector============#


# <input type="text" class="search-box-text ui-autocomplete-input" id="small-searchterms" autocomplete="off" name="q" placeholder="Search store" aria-label="Search store">

# ------- tag & id ----------#
# input_tag_id = driver.find_element(By.CSS_SELECTOR, "input#small-searchterms")--推薦唯一值機會較大
# input_tag_id  = driver.find_element(By.CSS_SELECTOR, "#small-searchterms")


# ------- tag & class ----------#
# input_tag_class = driver.find_element(
#     By.CSS_SELECTOR, "input.search-box-text")--推薦唯一值機會較大
# input_tag_class = driver.find_element(
#     By.CSS_SELECTOR, ".search-box-text")


# ------- tag & attribute ----------#
# input_tag_attribute = driver.find_element(
#     By.CSS_SELECTOR, "input[placeholder='Search store']")


# -------- tag & attribut & class -------#  唯一值機會最大
# input_tag_attribute_class = driver.find_element(
#     By.CSS_SELECTOR, "input.search-box-text[placeholder='Search store']")

input.send_keys("Laptop")


# input("Press Enter to close the browser...")
