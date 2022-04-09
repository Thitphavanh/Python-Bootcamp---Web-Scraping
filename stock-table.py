# stock-table.py
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=ptt&selectPage=2&max=180&offset=0'

webopen = urlopen(url)
pagehtml = webopen.read()
webopen.close()

data = BeautifulSoup(pagehtml, 'html.parser')

print(data.get_text())