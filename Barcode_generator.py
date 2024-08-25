import barcode
from barcode.writer import ImageWriter

text= "Python Barcode"
text1=str(text)
code= barcode.get_barcode_class("code128")
image= code(text,writer=ImageWriter())
save_path = r'C:\Users\Biswarup\Desktop\output\Final_barcode'
save_img = image.save(save_path)