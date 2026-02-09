import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in all_links:

    link_url = link.get_attribute("href")
    try:
        response = requests.head(link_url)
      # 檢查 HTTP 狀態碼是否為錯誤 (400 或以上)
        if response.status_code >= 400:
            print(f"失效連結 (狀態碼 {response.status_code}): {link_url}")
            count += 1
    except requests.exceptions.ConnectionError:
        # 捕捉像 DNS 查詢失敗這類的連線錯誤
        print(f"無法連線的連結 (名稱解析失敗或連線被拒): {link_url}")
        count += 1
    except requests.exceptions.RequestException as e:
        # 捕捉其他所有 requests 可能的錯誤，例如無效的 URL
        print(f"無效或格式錯誤的連結 ({e}): {link_url}")
        count += 1

input("Press Enter to close the browser...")
driver.quit()
