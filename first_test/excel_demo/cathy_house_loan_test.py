from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl


chrom_drive = webdriver.Chrome()
chrom_drive.get(
    "https://www.cathaybk.com.tw/cathaybk/personal/loan/calculator/mortgage-monthly-payments/")

chrom_drive.maximize_window()
wait_setting = WebDriverWait(chrom_drive, 10)


# ---- test data read from excel
excel_file = "D:\\selenium-driver\\ClassExamples\\ClassExamples\\caldata.xlsx"

workbook = openpyxl.load_workbook(excel_file)
sheet = workbook["Sheet2"]
