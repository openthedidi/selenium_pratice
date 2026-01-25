import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_drive = webdriver.Chrome()


chrom_drive.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
chrom_drive.maximize_window()

time.sleep(5)

link_href = chrom_drive.find_element(
    By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
link_href.click()

time.sleep(5)


# -----close()：
# 會關掉chrom_drive所代表的分頁(window)，其他從此分頁開啟的不受影響
# chrom_drive.close()


# -----quit()：
# 整個browser都會關掉，因為kill drive process了
# chrom_drive.quit()
#
