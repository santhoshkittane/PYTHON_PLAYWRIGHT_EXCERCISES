from qrcode import QRCode

url = input("Enter URL: ").strip()
file_path = "C:\\Users\\SanthoshKittane\\Desktop\\PYTHON\\QRCode.png"

qr= QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR Code Generated")
