import qrcode as qr
from PIL import Image  # import qrcode library

qrco=qr.QRCode(version=1,
               error_coorection=qr.constants.ERROR_CORRECT_H,
               box_size=10,border=4)
qrco.add_data("www.google.com")
qrco.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("newQrcode.jpg")
