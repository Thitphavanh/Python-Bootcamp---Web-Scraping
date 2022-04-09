# sendline.py
# pip install songline
import songline

linetoken = 'tozDy6Vk5rfxThnvQ4ZmEqPePxfJPnBhiRCoL4HzeIi'

message = songline.Sendline(linetoken)
# message.sendtext('ສະບາຍດີ')
message.sendimage('https://cdn-2.tstatic.net/tribunnews/foto/bank/images/liverpool_20181007_153951.jpg')