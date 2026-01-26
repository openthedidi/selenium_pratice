import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://www.skbank.com.tw/CC-Creditcard?page=&tags=&card_option=&international_organizations=")

wait_setting = WebDriverWait(
    chrom_drive, timeout=2, ignored_exceptions=Exception)

chrom_drive.maximize_window()

# ex：
# <a _ngcontent-serverapp-c129="" class="footer-sitemap__link h25" href="bf00beec15" target="_self" a-tag-href-routerlink-checker="">隱私政策</a>

link_btn = wait_setting.until(
    EC.presence_of_element_located((By.LINK_TEXT, "隱私政策")))
print(link_btn.text)
print(link_btn.is_enabled())

try:
    link_btn.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    print("使用 JavaScript 點擊來避免元素被遮擋的問題")
    chrom_drive.execute_script("arguments[0].click();", link_btn)

# ----------使用PARTIAL_LINK_TEXT，模糊找
link_btn2 = wait_setting.until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "安全")))
print(link_btn2.text)


input("Press Enter to close the browser...")
chrom_drive.quit()


#
