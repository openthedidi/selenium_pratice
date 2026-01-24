# locator分成兩種：
# 1. html檔案上面的屬性 (Attribute) 定位：(通常可以一眼就看出來)
#    - ID: 使用元素的 id 屬性，通常是唯一且最快的定位方式。
#    - Name: 使用元素的 name 屬性，常用於表單元素。
#    - Class Name: 使用元素的 class 屬性。
#    - Tag Name: 使用 HTML 標籤名稱 (例如 'div', 'a', 'input')。
#    - Link Text: 專門用於定位 <a> 標籤，使用完整的連結文字。
#    - Partial Link Text: 專門用於定位 <a> 標籤，使用部分的連結文字。

# 2. 結構/路徑 (Structure/Path) 定位：
#    - XPath: 使用 XML 路徑語言來撈全部的 HTML DOM 結構，功能強大但語法較複雜，速度相對較慢。
#    - CSS Selector: 使用 CSS 選擇器語法來定位元素，語法比 XPath 簡潔，執行速度通常比 XPath快。

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_drive = webdriver.Chrome()


chrom_drive.get(
    "https://demo.nopcommerce.com/")
chrom_drive.maximize_window()

time.sleep(5)

# <input type="text" class="search-box-text ui-autocomplete-input" id="small-searchterms" autocomplete="off" name="q" placeholder="Search store" aria-label="Search store">


# ---------- ID、NAME--------#
# search_input = chrom_drive.find_element(By.ID, "small-searchterms")
search_input = chrom_drive.find_element(By.NAME, "q")

search_input.clear()
search_input.send_keys("Laptop")


# ---------- Link-----------#
# <a href="/computers" aria-expanded="false" aria-haspopup="menu" role="button" class="menu__link" tabindex="0">Computers</a>

computer_menu = chrom_drive.find_element(
    By.LINK_TEXT, "Computers")
computer_menu2 = chrom_drive.find_element(
    By.PARTIAL_LINK_TEXT, "Compu")
# computer_menu = chrom_drive.find_element(By.XPATH, "//a[@href='/computers']")
# computer_menu.click()

# time.sleep(5)


# ==============  multi elements ================#
# ---------- by class name ------#
# <div class="swiper-slide swiper-slide-prev" style="width: 1200px; opacity: 1; transform: translate3d(0px, 0px, 0px); transition-duration: 0ms;" role="group" aria-label="1 / 2"><a href="https://demo.nopcommerce.com/apple-iphone-16-128gb"> <img class="slider-img" src="https://demo.nopcommerce.com/images/thumbs/0000079_banner_1.webp" loading="lazy"> </a></div>

sliders_list = chrom_drive.find_elements(
    By.CLASS_NAME, "swiper-slide")
# class name 如果登打複數的css，如(swiper-slide swiper-slide-prev)，會噴InvalidSelectorException: Message: Compound class names are not allowed

print(type(sliders_list))
print(len(sliders_list))

# 如果有複數element，但是call find_element，只會回傳第一個element
single_slider = chrom_drive.find_element(
    By.CLASS_NAME, "swiper-slide")


# ---------- by tag name ------#
herf_list = chrom_drive.find_elements(By.TAG_NAME, "a")
print(len(herf_list))
for herf in herf_list:
    print(herf.get_attribute("href"))


input("Press Enter to close the browser...")
