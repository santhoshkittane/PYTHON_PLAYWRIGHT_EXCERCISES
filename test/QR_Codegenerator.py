from qrcode import QRCode
from datetime import datetime
import URLMatching



url = input("Enter URL: ").strip()
web_name = URLMatching.get_website_name(url)
print(web_name)
now = web_name+"-QRCode-"+str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+".png"
print(now)
if URLMatching.urlmatch(url):
    file_path = "C:\\Users\\SanthoshKittane\\Desktop\\PYTHON\\"+now

    qr= QRCode()
    qr.add_data(url)

    img=qr.make_image()
    img.save(file_path)

    print("QR Code Generated")

else:
    print("Invalid URL")
