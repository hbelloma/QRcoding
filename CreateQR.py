#! /usr/bin/python3
# to do first install: pip install qrcode[pil]
import qrcode
import pyqrcode
import pandas as pd

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

def createQRSimple():
    data = 'your text here'
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    #you can Skip all behind with the following line
    #img = qrcode.make(input('What should the QR code say? '))
    img.save('saved.png')
    img.show('saved.png') #You can remove this line if you do not need to see a preview after QR generation


def createQRCode():


    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

        brand = values["Brand"]
        name = values["Name"]
        category = values["Category"]
        barcode = values["Barcode"]

        data = f'''

        Name: {name} \n
        Barcode: {barcode} \n
        Category: {category} \n
        Brand: {brand}
        '''
        image = pyqrcode.create(data)
        image.svg(f"{name}_{barcode}.svg", scale="5")
        print(data)



createQRCode()



