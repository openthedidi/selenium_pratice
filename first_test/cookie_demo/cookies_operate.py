from selenium import webdriver


chrom_drive = webdriver.Chrome()

chrom_drive.get(
    "https://www.nanshanlife.com.tw/nanshanlife/contact-us")

print(chrom_drive.title)
cookies_list = chrom_drive.get_cookies()
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


chrom_drive.add_cookie({"name": "mark", "value": "mark!!"})


cookies_list = chrom_drive.get_cookies()
print("----add----")
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


chrom_drive.delete_cookie("mark")
cookies_list = chrom_drive.get_cookies()
print("----delete----")
print(len(cookies_list))
for cookie in cookies_list:
    print(cookie['name'], cookie['value'])


chrom_drive.quit()
