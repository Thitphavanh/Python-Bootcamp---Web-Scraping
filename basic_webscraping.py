#basic-webscraping.py
from urllib.request import urlopen as req # as req ແມ່ນ ການຂຽນຊື່ຫຍໍ້
from bs4 import BeautifulSoup as soup

def StockPrice(CODE='PTT'):

	url = f'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={CODE}&ssoPageId=10&selectPage=2'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html, 'html.parser')
	result = data.find_all('div', {'class':'col-xs-6'})

	title = result[0].text
	price = float(result[2].text)
	change = result[3].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	change = float(change[11:]) # ຕັດຄຳວ່າ ປ່ຽນແປງ ອອກໄປ
	perchange = result[4].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	perchange = float(perchange[12:-1]) # ຕັດຄຳວ່າ %ປ່ຽນແປງ ແລະ % ດ້ານຫຼັງອອກໄປ

	print('Stock : {}, Price : {}, Change : {}, %Change : {}'.format(title, price, change, perchange))
	return (title,price,change,perchange)

Kbank = StockPrice('KBANK')
print(Kbank[1] * 15200)
StockPrice('KBANK')
StockPrice('SCB')
StockPrice('TTB')

