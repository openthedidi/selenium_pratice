from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_chrome_driver():
    # --- 設定檔案下載的路徑，沒有設定就是吃預設
    preference = {"download.default_directory": "D:\\selenium-driver",
                  "plugins.always_open_pdf_externally": True,
                  "download.prompt_for_download": False}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preference)
    return webdriver.Chrome(options=ops)


def get_edge_driver():
    # --- 設定檔案下載的路徑，沒有設定就是吃預設
    preference = {"download.default_directory": "D:\\selenium-driver",
                  "plugins.always_open_pdf_externally": True,
                  "download.prompt_for_download": False}

    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preference)
    return webdriver.Edge(options=ops)


def get_firefox_driver():
    # ---設定檔案下載的路徑，沒有設定就是吃預設

    ops = webdriver.FirefoxOptions()

    # 0: 將檔案儲存在桌面。
    # 1: 將檔案儲存在預設的「下載」資料夾中。
    # 2: 將檔案儲存在上次使用的資料夾或指定的自訂資料夾。
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", "D:\\selenium-driver")
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk",
                       "application/octet-stream")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("pdfjs.disabled", True)

    return webdriver.Firefox(options=ops)


def select_drive(target):
    if target == "chrome":
        return get_chrome_driver()
    elif target == "edge":
        return get_edge_driver()
    elif target == "firefox":
        return get_firefox_driver()
    else:
        return None


# drive = select_drive("chrome")
# drive = select_drive("edge")
drive = select_drive("firefox")
# drive.get("https://www.fileexamples.com/category/spreadsheet")
drive.get("https://www.fileexamples.com/category/document")
drive.maximize_window()


time.sleep(2)

# btn_download = drive.find_element(
#     By.XPATH, "/html/body/div[2]/main/div/div[2]/div[1]/div[2]/a[2]")
btn_download_pdf = drive.find_element(
    By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/div[2]/a[2]")
btn_download_pdf.click()


time.sleep(5)  # 等待下載
drive.quit()  # 使用正確的 drive 變數關閉瀏覽器
