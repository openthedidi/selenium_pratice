import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)

# frame(name of the frame)
driver.switch_to.frame("packageListFrame")
# frame(id of the frame)
# frame(index of the frame)

link_in_first_frame = driver.find_element(By.LINK_TEXT, "java.awt.dnd")
link_in_first_frame.click()

# ========frame 之間的輪轉都要先切回預設
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
link_in_second_frame = driver.find_element(By.LINK_TEXT, "Autoscroll")
link_in_second_frame.click()

driver.quit()


# ===========  inner frame結構  =============


driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(
    By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

first_frame = driver.find_element(
    By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(first_frame)

second_frame = driver.find_element(
    By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(second_frame)

input = driver.find_element(By.XPATH, "//input[@type='text']")
input.send_keys("test")

driver.quit()
