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
    chrom_drive, timeout=3, ignored_exceptions=Exception)


filter_btn = wait_setting.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@class='filter-composition__filter-btn-text h36']")
))
filter_btn.click()


# wait_setting.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//div[normalize-space()='頂級卡']/ancestor::label"))
# ).click()

# top_checkbox = wait_setting.until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='card_option-111']"))
# )
# top_checkbox.click()

wait_setting.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "label[for='card_option-111']"))
).click()

# example html
# <input _ngcontent-serverapp-c181="" type="checkbox" class="filter-button__checkbox ng-untouched ng-valid ng-dirty" id="card1-300101">
# <label _ngcontent-serverapp-c181="" class="filter-button__content" for="card1-300101"><div _ngcontent-serverapp-c181="" class="filter-button__text h23"> 現金回饋 </div></label>


# special checkbox
spec_checkboxs = chrom_drive.find_elements(
    By.XPATH, "//div[@class='filter-criteria-item__content']//label[contains(@for,'300')]")

print(len(spec_checkboxs))
for checkbox in spec_checkboxs:
    # 使用 JavaScript 點擊來避免元素被遮擋的問題
    chrom_drive.execute_script("arguments[0].click();", checkbox)
    print(f"成功點擊: {checkbox.text}")


# clear checkbox


time.sleep(2)

checked_labels = chrom_drive.find_elements(
    By.XPATH, "//div[@class='filter-criteria-item__content']//label[contains(@for,'300')]")
print(len(checked_labels))


# 如果是checkbox是用其他校label顯示，要採用execute_script執行勾選，且檢查方式還是要用input元素

for checked_label in checked_labels:
    print(checked_label.is_selected())
    target_id = checked_label.get_attribute("for")
    # label對應的checkbox
    checkedbox = chrom_drive.find_element(
        By.XPATH, f"//input[@id='{target_id}']")
    # 檢查是否勾選還是要用input
    if checkedbox.is_selected():
        chrom_drive.execute_script("arguments[0].click();", checked_label)
        print("取消勾選")


input("Press Enter to close the browser...")
chrom_drive.quit()
