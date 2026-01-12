import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=100,
    border=4
)
data=input("Enter your qr code link :")
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black")
img.save("my_qr.png")

print("QR Code created")
