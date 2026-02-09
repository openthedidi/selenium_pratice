from selenium import webdriver


driver = webdriver.Chrome()

driver.get(
    "https://www.nanshanlife.com.tw/nanshanlife/contact-us")

print(driver.title)
cookies_list = driver.get_cookies()
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


driver.add_cookie({"name": "mark", "value": "mark!!"})


cookies_list = driver.get_cookies()
print("----add----")
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


driver.delete_cookie("mark")
cookies_list = driver.get_cookies()
print("----delete----")
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


driver.quit()
