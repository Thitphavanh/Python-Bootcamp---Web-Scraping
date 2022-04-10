# twitter.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ລະບຸຕຳແໜ່ງ webdriver
path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\WebScraping\chromedriver_win32\chromedriver.exe'
ser = Service(path)


# don't open google chrome
# opt = webdriver.ChromeOptions()
# opt.add_argument('headless')

options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument("start-maximized")
options.add_argument('--enable-javascript')

# ສ້າງ driver
driver = webdriver.Chrome(service=ser, options=options)

# url ເລີ່ມຕົ້ນ
# url = 'https://twitter.com/bbcworld'
# url = 'https://twitter.com/Thairath_News'
url = 'https://twitter.com/MatichonOnline'
driver.get(url)

time.sleep(5)
# css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

#############LOAD DATA###########
start = 20000  # ເລີ່ມຕົ້ນຄັ້ງທຳອິດ
end = 80001  # ເພີ່ມຈຳນວນນີ້ເພື່ອໃຫ້ໄດ້ຜົນລັບຫຼາຍຂຶ້ນ
step = 20000  # ຍັບໄປຄັ້ງລະ 20,000

for i in range(start, end, step):
    # ຣັນ script ໃຫ້ຍັບລົງມາ
    driver.execute_script('window.scrollTo(0,{})'.format(i))
    time.sleep(3)
    html = driver.page_source
    data = BeautifulSoup(html, 'html.parser')
    # print(data.get_text())

    post = data.find_all(
        'span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

    prev = ''

    result_post = []

    for p in post:
        if prev == '·':
            # print(p.text)
            result_post.append(p.text)
            # print('-------------')
        prev = p.text

    # print('=============LINK=============')
    link = data.find_all(
        'a', {'class': 'css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0'})

    result_link = []

    for l in link:
        # print(l)
        result_link.append('https://twitter.com' + l['href'])
        # print('-----')
    # print('=============================')

    for i, (x, y) in enumerate(zip(result_post, result_link), start=1):
        print(i)
        print(x)
        print(y)
        print('---------')
