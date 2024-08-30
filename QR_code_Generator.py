import qrcode as qr
from PIL import Image  # import qrcode library

qrco=qr.QRCode(version=1,
               error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10,border=4)
qrco.add_data("www.google.com")
qrco.make(fit=True)
img=qrco.make_image(fill_color="red",back_color="blue")
save_path = r'C:\Users\Biswarup\Desktop\output\Final_Qr.png'
img.save(save_path)
