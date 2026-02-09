from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
# 導入 WebDriverWait 和 expected_conditions，for「顯性等待」
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 開啟瀏覽器-方法一，不指定路徑
# 根據驅動程式的版本號建立資料夾，
# 同時保留多個版本的驅動程式，
# 並根據本機安裝的瀏覽器版本自動選用最匹配的一個。

driver = webdriver.Chrome()


# 開啟瀏覽器-方法二，指定路徑
# 1. 建立 Service 物件並傳入 driver 路徑，如果drive的版本與browser版本不同，
# 就會出現selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version
# service_obj = Service("D:\\selenium-driver\\driver\\chromedriver.exe")

# 2. 將 Service 物件傳遞給 webdriver.Chrome
# driver = webdriver.Chrome(service=service_obj)


driver.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)  # 暫停5秒，等待頁面載入

# 使用顯性等待，等待最多10秒，直到 name='username' 的元素出現
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("admin123")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    title = driver.title
    if (title == "OrangeHRM"):
        print("login success")
    else:
        print("login fail")

    driver.close()


except Exception as e:
    print(f"找不到元素，錯誤: {e}")

# driver.find_element(By.NAME, "password").send_keys("admin123")
# 使用 XPath 根據 type='submit' 屬性來定位登入按鈕
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# 使用 . 來代表 class
# driver.find_element(By.CSS_SELECTOR, ".login-button")


# 讓程式暫停，等待使用者在 console 按下 Enter 鍵後才繼續執行
# 這樣可以防止瀏覽器視窗自動關閉
# input("Press Enter to close the browser...")
