import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.misin.msu.edu/0/js/DataTablesP/DataTables-1.10.18/examples/api/tabs_and_scrolling.html")

wait = WebDriverWait(driver, 10, 2)

scrollTableDiv = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//div[@class='dataTables_scrollBody']")))


driver.execute_script("arguments[0].scrollBy(0, 1000);", scrollTableDiv)
time.sleep(3)

driver.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight;", scrollTableDiv)
time.sleep(3)

driver.execute_script("arguments[0].scrollTop=0;", scrollTableDiv)

driver.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight/2;", scrollTableDiv)

driver.execute_script("arguments[0].scrollLeft = 200;", scrollTableDiv)

target_info = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//table[@id='myTable1']//td[text()='Dai Rios']")))

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", target_info)


time.sleep(3)

#
