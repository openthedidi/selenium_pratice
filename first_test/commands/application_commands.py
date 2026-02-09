from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# ========= get()==========
driver.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title)
print(driver.current_url)

# ------ source code，有時候不會是完整的html-----
# 因為頁面會使用 JavaScript 在背景非同步地（Asynchronously）載入更多內容或修改現有結構。
print(driver.page_source)


# 等待登入按鈕出現，這表示頁面的主要 JavaScript 已經執行完畢
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@type='submit']"))
)
print("--after wait--")
print(driver.page_source)


driver.quit()
