#pip install Pillow (Python Imaging Library),qrcode 

import qrcode as qr

query=input("Enter the link to make the qr: ")

# To create the qrcode for the given query qr.make  function is used 
img=qr.make(query)
# To save the image with name qrcode.png
img.save("qrcode.png")