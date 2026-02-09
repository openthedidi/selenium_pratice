from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get(
    "https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)


time.sleep(3)


sliders = wait_setting.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")))

left_slider = sliders[0]
right_slider = sliders[1]

print(left_slider.location)
print(right_slider.location)


act = ActionChains(driver)
act.drag_and_drop_by_offset(left_slider, 50, 0).perform()
act.drag_and_drop_by_offset(right_slider, -20, 0).perform()


time.sleep(3)
print(left_slider.location)
print(right_slider.location)

input("Press Enter to close the browser...")
driver.quit()
