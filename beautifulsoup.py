
from bs4 import BeautifulSoup
title = '<html> <title>ABC</title><html>'
box = BeautifulSoup(title, 'html.parser')
box
<html > <title > ABC < /title > <html > </html > </html >
box.title
<title > ABC < /title >
box
<html > <title > ABC < /title > <html > </html > </html >
type(box)
<class 'bs4.BeautifulSoup' >
box.title.text
'ABC'
