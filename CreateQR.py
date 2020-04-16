#! /usr/bin/python3
# to do first install: pip install qrcode[pil]

import qrcode
img = qrcode.make(input('What should the QR code say? '))
img.save('saved.png')

img.show('saved.png') #You can remove this line if you do not need to see a preview after QR generation
