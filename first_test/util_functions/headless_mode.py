from selenium import webdriver
from selenium.webdriver.common.by import By


def get_headless_chrome_driver():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver


def get_headless_edge_driver():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless=new")
    edge_drive = webdriver.Edge(options=ops)
    return edge_drive


def get_headless_firefox_driver():
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless=new")
    firefox_drive = webdriver.Firefox(options=ops)
    return firefox_drive


# drive = get_headless_edge_driver()
# drive = get_headless_chrome_driver()
drive = get_headless_firefox_driver()
drive.get("https://www.taiwanlife.com/index")
drive.maximize_window()

print(drive.title)
print(drive.current_url)

drive.quit()
