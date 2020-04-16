#! /usr/bin/python3
# to do first install: pip install qrcode[pil]
import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)
data = 'your text here'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

#you can Skip all behind with the following line
#img = qrcode.make(input('What should the QR code say? '))
img.save('saved.png')

img.show('saved.png') #You can remove this line if you do not need to see a preview after QR generation

