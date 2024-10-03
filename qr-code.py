# 1. Atver "Terminal" logu (Terminal -> New Terminal) un ielādē bibliotēku "qrcode" ar komandas palidzību
# > pip install qrcode
# 
# 2. Palaid kodu, nolasi kodu ar sava telefona kameru
#
# 3. Pamaini kodu lai teksts būtu prasīts no lietotāja (input())
#
# 4. Izmantojot bibliotēkas dokumentāciju, uzraksti kodu lai tiktu ģenerēts QR kods ar šādiem parametriem:
# https://github.com/lincolnloop/python-qrcode
# - teksts tiek prasīts no lietotāja
# - border izmērs - 5
# - koda izmērs - 20
# - kļūdu labojums - Q
# - stils - vertikāls gradients (VerticalGradiantColorMask)
#

import qrcode
img = qrcode.make('Hello 72 vsk')
img.show()
