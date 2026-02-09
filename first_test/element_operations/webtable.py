from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ============ static table =============
driver = webdriver.Chrome()
driver.get(
    "https://www.moneydj.com/etf/x/basic/basic0003.xdjhtm?etfid=QQQ")

driver.maximize_window()


table_tbody_tr_list = driver.find_elements(
    By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//tr")

# print(f"row amounts : {len(table_tbody_tr_list)}")
for tr in table_tbody_tr_list:
    print(tr.text)


table_tbody_th_list = driver.find_elements(
    By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//th")

# print(f"columns amounts : {len(table_tbody_th_list)}")
for th in table_tbody_th_list:
    print(th.text)

data1 = driver.find_element(
    By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//tr[2]//td[2]")
# print(data1.text)


all_title = driver.find_elements(
    By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//tr//th")

all_data = driver.find_elements(
    By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//tr//td")


for r in range(1, len(table_tbody_tr_list)):
    r += 1
    for c in range(1, len(table_tbody_th_list)):
        data = driver.find_element(
            By.XPATH, "//table[@id='ctl00_ctl00_MainContent_MainContent_stable']//tbody//tr" + str([r]) + "//td" + str([c]))
        print(data.text, end=" ")
        c += 1
    print()

driver.quit()

# ============ dynamic table =============


def str_persent_2_float(target):
    # 把字串的例如+0.70%，轉成0.7
    return float(target.replace("%", ""))


driver = webdriver.Chrome()
driver.get("https://www.cmoney.tw/forum/fund/rank/bond")

three_month_btn = driver.find_element(
    By.XPATH, "//div[contains(text(),'3個月')]")
three_month_btn.click()

time.sleep(5)


all_data_list_by_rows = driver.find_elements(
    By.XPATH, "//tbody[@class='fund-ranking-list__tbody']//tr")

print(f"總共找到 {len(all_data_list_by_rows)} 列資料")

for row in all_data_list_by_rows:

    product_name_element = row.find_element(By.XPATH, ".//td[2]")
    data_element = row.find_element(By.XPATH, ".//td[4]")

    product_name = product_name_element.text
    data_text = data_element.text

    if str_persent_2_float(data_text) > 20:
        print(f"product: {product_name}, data: {data_text}")
        print("\n")


input("Press Enter to close the browser...")
