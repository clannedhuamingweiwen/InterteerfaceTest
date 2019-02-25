#coding:utf-8
from  PIL import Image
import pytesseract as p
text = p.image_to_string(Image.open(r"C:\Users\win10\Desktop\img\1.png"),lang='chi_sim')

print text



