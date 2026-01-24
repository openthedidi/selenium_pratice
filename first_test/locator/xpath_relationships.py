

# 可以從一個已定位的節點出發，去尋找它周圍有特定關係的其他節點。


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nanshanlife.com.tw/nanshanlife/products-health")
driver.maximize_window()
time.sleep(5)

# -----------self------------

self = driver.find_element(
    By.XPATH, "//li[contains(text(),'安寧療護')]/self::li")
print(self.text)


# ----------parent-----------
# 與self以上的直屬一階層級
parent = driver.find_element(
    By.XPATH, "//li[contains(text(),'安寧療護')]/parent::ul")

print(parent.tag_name)  # print ul
print(parent.text)  # print ul 下面所有 li 的可見文字合併


# ----------child-----------
# 與self以下的直屬一階層級
child_li = driver.find_elements(
    By.XPATH, "//li[contains(text(),'安寧療護')]/ancestor::div/child::ul")
print(len(child_li))

for li in child_li:
    print(li.tag_name)
    print(li.text)

# ----------ancestor-----------
# ancestor後面的html tag樣式決定相同的祖先數量

ancestors = driver.find_elements(
    By.XPATH, "//li[contains(text(),'安寧療護')]/ancestor::nanshan-product-card")
print("----ancestor-----")
print(len(ancestors))

for ancestor in ancestors:
    print(ancestor.tag_name)
    print(ancestor.text)

# ----------descendant-----------
# 與self以下的全部層級
# [x] x決定抓取的數量
descendant = driver.find_elements(
    By.XPATH, "//li[contains(text(),'安寧療護')]/ancestor::div/child::ul/descendant::li[1]")
print(len(descendant))

for li in descendant:
    print(li.tag_name)
    print(li.text)

descendant_type2 = driver.find_elements(
    By.XPATH, "//li[contains(text(),'安寧療護')]/ancestor::div/child::ul/descendant::*")
print(len(descendant_type2))


# ---------following-------------
# 不含parent，只有與parent的平行之後的層級與self平行且之後的層級

following = driver.find_elements(
    By.XPATH, "//li[contains(text(),'安寧療護')]/ancestor::div/following::*")
print(len(following))

# -------following-sibling-------
# 與self平行及之後的層級
following_siblings = driver.find_elements(
    By.XPATH, "//div[contains(text(),'南山人壽長青安溢醫療定期健康保險')]/following-sibling::*")
print(len(following_siblings))

for following_sibling in following_siblings:
    print(following_sibling.tag_name)
    print(following_sibling.text)


# --------preceding------------
# 不含parent，只有與parent的平行以前的層級與self平行且以前的層級

preceding = driver.find_elements(
    By.XPATH, "//div[contains(text(),'特定人工關節補助金')]/preceding::*")
print(len(preceding))


# --------preceding-sibling------------
# 與self平行及以前的層級

preceding_sibling = driver.find_elements(
    By.XPATH, "//div[contains(text(),'特定人工關節補助金')]/preceding-sibling::*")
print(len(preceding_sibling))
for preceding_sib in preceding_sibling:
    print(preceding_sib.tag_name)
    print(preceding_sib.text)
