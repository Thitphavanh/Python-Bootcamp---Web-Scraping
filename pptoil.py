# pptoil.py

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ລະບຸຕຳແໜ່ງ webdriver
path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\WebScraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)


# don't open google chromw
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

# ສ້າງ driver
driver = webdriver.Chrome(service=ser, options=opt)


# url ເລີ່ມຕົ້ນ
url = 'https://www.pttor.com/th/oil_prices/'
driver.get(url)

allresult = []

for i in range(2, 5):
    dropdown = driver.find_element(By.XPATH, '//*@id="__layout"]/div/div/section/div[2]/div/div/div[2]/form/div[2]/select/option[{}]')
    dropdown.click()
    time.sleep(1)
    table = driver.find_element(By.TAG_NAME, 'table')
    row = table.find_elements(By.TAG_NAME, 'tr')

    for r in row:
        column = r.find_elements(By.TAG_NAME, 'td')
        day = []
        for c in column:
            # print(c.text)
            day.append(c.text)
        print(day)
        if len(day) != 0:
            allresult.append(day)
    # print(table.text)
    print('-----------')

print(allresult)
driver.close()
