import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://docs.oracle.com/javase/8/docs/api/")
chrom_drive.maximize_window()

wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)

# frame(name of the frame)
chrom_drive.switch_to.frame("packageListFrame")
# frame(id of the frame)
# frame(index of the frame)

link_in_first_frame = chrom_drive.find_element(By.LINK_TEXT, "java.awt.dnd")
link_in_first_frame.click()

# ========frame 之間的輪轉都要先切回預設
chrom_drive.switch_to.default_content()

chrom_drive.switch_to.frame("packageFrame")
link_in_second_frame = chrom_drive.find_element(By.LINK_TEXT, "Autoscroll")
link_in_second_frame.click()

chrom_drive.quit()


# ===========  inner frame結構  =============


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://demo.automationtesting.in/Frames.html")
chrom_drive.maximize_window()

chrom_drive.find_element(
    By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

first_frame = chrom_drive.find_element(
    By.XPATH, "//iframe[@src='MultipleFrames.html']")
chrom_drive.switch_to.frame(first_frame)

second_frame = chrom_drive.find_element(
    By.XPATH, "//iframe[@src='SingleFrame.html']")
chrom_drive.switch_to.frame(second_frame)

input = chrom_drive.find_element(By.XPATH, "//input[@type='text']")
input.send_keys("test")

chrom_drive.quit()
