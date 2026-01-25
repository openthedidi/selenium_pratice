from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrom_drive = webdriver.Chrome()

# ========= get()==========
chrom_drive.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(chrom_drive.title)
print(chrom_drive.current_url)

# ------ source code，有時候不會是完整的html-----
# 因為頁面會使用 JavaScript 在背景非同步地（Asynchronously）載入更多內容或修改現有結構。
print(chrom_drive.page_source)


# 等待登入按鈕出現，這表示頁面的主要 JavaScript 已經執行完畢
WebDriverWait(chrom_drive, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@type='submit']"))
)
print("--after wait--")
print(chrom_drive.page_source)


chrom_drive.quit()
