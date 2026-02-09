import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.taiwanlife.com/index")

driver.maximize_window()

wait_setting = WebDriverWait(driver, 10)

en_link = wait_setting.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(.,'EN')]")))

# --------方法一
# en_link.send_keys(Keys.CONTROL + Keys.RETURN)

# --------方法二
act = ActionChains(driver)
act.key_down(Keys.CONTROL).click(en_link).key_up(Keys.CONTROL).perform()


time.sleep(5)

driver.quit()
