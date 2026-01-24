# 2. 結構/路徑 (Structure/Path) 定位：
#    - XPath: 使用 XML 路徑語言來撈全部的 HTML DOM 結構，功能強大但語法較複雜，速度相對較慢。


# =========== absolute/Full xpath ============#
# /html/body/nav/div/div/ul[2]/li[2]/a/button:
# 代表xpath的階層路徑；[2]:代表同名節點且平行階層中的第二個

# =========== relative/partial xpath  ============#
# //*[@id="navbarNav"]/ul[2]/li[2]/a/button
# xpath的階層路徑，但是會從可以定位到指定元素的父層元素開始起算，並且使用父層元素的Attribute，好處是當網頁前端結構有小幅變動時，相對 XPath 的定位腳本也比較不容易失效。

# // 的意思是「從文件的任何位置開始搜索」， *[@id="navbarNav"] 的意思是尋找任何標籤(*) 且 id 屬性等於 "navbarNav" 的元素。

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrom_drive = webdriver.Chrome()


chrom_drive.get(
    "https://www.nanshanlife.com.tw/nanshanlife/")
chrom_drive.maximize_window()

time.sleep(5)

#

# search_btn = chrom_drive.find_element(
#     By.XPATH, "//div[@class='header__search-open-icon ng-tns-c121-0']//nxtle-icon[@class='ng-tns-c121-0']//*[name()='svg']")

search_btn = chrom_drive.find_element(
    By.XPATH, "/html/body/app-root/rdr-render/rdr-templates-container/rdr-dynamic-wrapper/nanshan-portal-layout/nanshan-empty-layout/div/nxtle-full-height-layout/div/div[1]/div/nanshan-header-template/nanshan-header/header/div[2]/div/div[2]/button[1]")


search_btn.click()

search_input = chrom_drive.find_element(
    By.XPATH, "//div[@class='header-search__search-box']//input[@id='search']")

search_input.send_keys("20")

search_btn_star = chrom_drive.find_element(
    By.XPATH, "//button[@class='input-search-bar__search-button-submit']//nxtle-icon[@icon='search']//*[name()='svg']")

search_btn_star.click()

#

input("Press Enter to close the browser...")
