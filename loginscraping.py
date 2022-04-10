# loginscraping.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ລະບຸຕຳແໜ່ງ webdriver
path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\WebScraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)

# ສ້າງ driver
driver = webdriver.Chrome(service=ser)


# url ເລີ່ມຕົ້ນ
url = 'http://uncle-machine.com/login/'
driver.get(url)


# ຄົ້ນຫາ element ໃນການລ໋ອກອິນ
username = driver.find_element(By.ID, 'username')
username.send_keys('thitphavanh23@gmail.com')
