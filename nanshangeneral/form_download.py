from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config.browser_settings import BrowserSettings


chrom_drive = BrowserSettings().get_chrome_driver(maximize=True)
chrom_drive.get(
    "https://www.nanshangeneral.com.tw/download")

wait_setting = WebDriverWait(chrom_drive, 3)


form_catagory_select = wait_setting.until(EC.presence_of_element_located(
    (By.XPATH, '//span[text()="全類別"]')))

chrom_drive.execute_script("arguments[0].click();", form_catagory_select)


input("123")
chrom_drive.quit()
