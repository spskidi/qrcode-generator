import qrcode
qr = qrcode.QRCode(
    version=20,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=4,
)
query=input("Enter the link for which qr has to make : ")
filename=input('Enter the file name (include.png also at last)')
qr.add_data(query)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
