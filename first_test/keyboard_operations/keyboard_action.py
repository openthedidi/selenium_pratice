from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_drive = webdriver.Chrome()
chrome_drive.get("https://text-compare.com/")

chrome_drive.maximize_window()

time.sleep(2)


chrome_drive.find_element(
    By.NAME, "text1").send_keys("Hello World")
input_area2 = chrome_drive.find_element(By.NAME, "text2")


act = ActionChains(chrome_drive)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()

act.move_to_element(input_area2).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


input("1231")

chrome_drive.quit()
