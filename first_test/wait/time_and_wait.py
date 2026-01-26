import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://www.skbank.com.tw/search")
chrom_drive.maximize_window()

# time 的壞處：
# 1.每次都要等時間到 2.如果時間到element還不能互動就會噴exption
# time.sleep(5)

# implicitly wait：以下的腳本都會自動適用，且如果元素或是頁面還不可用，最久的時間內都可以
# chrom_drive.implicitly_wait(5)

# explicit wait
# parameter:
wait_setting = WebDriverWait(
    chrom_drive, timeout=10, ignored_exceptions=Exception, poll_frequency=0.5)

search_input = None  # 先將變數初始化為 None

element_is_present = EC.presence_of_element_located(
    (By.XPATH, "//input[@id='siteSearchKeyword']"))

if element_is_present:
    search_input = wait_setting.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='siteSearchKeyword']"))
    )
    search_input.clear()
    search_input.send_keys("20")
    print("成功輸入文字到搜尋框！")
elif search_input is None:
    print("element is not present.")

    chrom_drive.quit()
