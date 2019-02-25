import Image,ImageFilter
file=r"C:\Users\win10\PycharmProjects\InterteerfaceTest\utilititys\test.jpg"
im=Image.open(file)
im2=im.filter(ImageFilter.BLUR)
im2.save(r"C:\Users\win10\PycharmProjects\InterteerfaceTest\utilititys\bur.jpg","jpeg")

