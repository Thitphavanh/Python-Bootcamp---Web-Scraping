# matichon.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.bangkokpost.com/business/'
# url = 'https://www.matichon.co.th/sport'

webopen = urlopen(url)
pagehtml = webopen.read().decode('utf-8')
webopen.close()


data = BeautifulSoup(pagehtml, 'html.parser')

news_row = data.find_all('div', {'class':'listnews-text'})
print(news_row[0].h3.a['href'])

for n in news_row:
    print(n.h3.text)
    print(n.p.text)
    print('https://www.bangkokpost.com' + n.h3.a['href'])
    print('----------')

