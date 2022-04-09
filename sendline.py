# sendline.py
# pip install songline
import songline
linetoken = 'tozDy6Vk5rfxThnvQ4ZmEqPePxfJPnBhiRCoL4HzeIi'
message = songline.Sendline(linetoken)
# message.sendtext('ສະບາຍດີ')
# message.sendimage('https://i0.wp.com/crowdwisdom.live/wp-content/uploads/2021/09/Liverpool-vs-Man-City-Prediction-and-Odds.jpg')
message.sticker(513,2)