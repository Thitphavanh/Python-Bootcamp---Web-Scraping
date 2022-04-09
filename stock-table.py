# stock-table.py
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=ptt&selectPage=2&max=180&offset=0'

webopen = urlopen(url)
pagehtml = webopen.read()
webopen.close()

data = BeautifulSoup(pagehtml, 'html.parser')

# print(data.get_text())

table = data.find('table',{'class':'table table-info table-hover'})
# ຖ້າມີ table ທີ່ມີຊື່ຄລາສນີ້ພຽງຄລາສດຽວ ສາມາດໃຊ້ .find ໄດ້ ທີ່ຈະອອກມາແຕ່ ລາຍການ ບໍ່ຕ້ອງຣັນລູປ

table = table.find_all('tr')[1:]
# print(table)

result = []

for row in table:
	column = row.find_all('td')
	# print(column)
	column_list = []
	for i,c in enumerate(column):
		if i!= 0:
			column_list.append(float(c.text.replace(',','')))
		else:
			column_list.append(c.text)
	print(column_list)
	print('-------')

