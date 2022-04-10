# loginscraping.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ລະບຸຕຳແໜ່ງ webdriver
path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\WebScraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)


# don't open google chromw
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

# ສ້າງ driver
driver = webdriver.Chrome(service=ser, options=opt)


# url ເລີ່ມຕົ້ນ
url = 'http://uncle-machine.com/login/'
driver.get(url)


# ຄົ້ນຫາ element ໃນການລ໋ອກອິນ
username = driver.find_element(By.ID, 'username')
username.send_keys('thitphavanh23@gmail.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('hery18205208038')

# password.send_keys(Keys.RETURN)
# Button by xpath
btn_xpath = '/html/body/div[2]/form/button'
btn = driver.find_element(By.XPATH, btn_xpath)
btn.click()


# ------------Sensor------------
url_sensor = 'http://uncle-machine.com/sensor/'
driver.get(url_sensor)

sid = driver.find_element(By.NAME, 'sid')
sid.send_keys('TM-1001')
sid.send_keys(Keys.RETURN)


# ------------ຄົ້ນຫາ Selenium------------
temp = driver.find_element(By.CLASS_NAME, 'temp')
humid = driver.find_element(By.CLASS_NAME, 'humid')
print('{} {}'.format(temp.text, humid.text))


# ------------ຄົ້ນຫາ bs4------------
html = driver.page_source  # show source code html
data = BeautifulSoup(html, 'html.parser')

temp2 = data.find('div', {'class': 'temp'}).text
humid2 = data.find('div', {'class': 'humid'}).text

print('{} {}'.format(temp2, humid2))

print('----------')

print(data.get_text())

text = data.get_text()

with open('export.txt', 'w', encoding='utf-8') as file:
    file.write(text)

driver.close()
