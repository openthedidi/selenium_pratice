import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    "https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)


driver.execute_script("window.scrollTo(0, 200);")


span_btn = wait_setting.until(
    EC.presence_of_element_located((By.XPATH, "//span[@id='select2-billing_country-container']")))
span_btn.click()

time.sleep(3)

option_btn_list = wait_setting.until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='select2-results__options']//li[@class='select2-results__option']")))

for option_btn in option_btn_list:
    if (option_btn.text == "Yemen"):
        option_btn.click()
        break


input("Press Enter to close the browser...")
driver.quit()


#
