import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_drive = webdriver.Chrome()


chrom_drive.get(
    "https://www.nanshanlife.com.tw/nanshanlife/service-faq")
chrom_drive.maximize_window()

time.sleep(5)

# ===========  or   ===========

btns = chrom_drive.find_elements(
    By.XPATH, "//button[@class='hot-search-button-bar__button h15' or @type='button']")

print(len(btns))

for btn in btns:
    print(btn.text)

# ===========  and   ===========

btns2 = chrom_drive.find_elements(
    By.XPATH, "//button[@class='hot-search-button-bar__button h15' and @type='button']")

print(len(btns2))

for btn in btns2:
    print(btn.text)


# ========== contains ============

btns3 = chrom_drive.find_elements(
    By.XPATH, "//button[contains(.,'保單')]")
print(len(btns3))

# btn3_5 = chrom_drive.find_element(
#     By.XPATH, "//div[contains(@id,'event')]")
# print(btn3_5.text)


# ========== starts-with==========

btns4 = chrom_drive.find_elements(
    By.XPATH, "//button[starts-with(@class,'hot-search-button-bar')]")
for btn in btns4:
    print(btn.text)

print(len(btns4))


# ========= text()=============

divs = chrom_drive.find_elements(By.XPATH, "//div[text()='熱門搜尋']")
print(len(divs))


#
