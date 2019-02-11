from PIL import Image

img = Image.open("Test.jpg")

sizewidth = 0
sizeheight = 0
counter = 100
counter_height = 0

while img.width > sizewidth:
    sizeheight = counter_height * 300
    left, top, width, height = sizewidth, sizeheight, sizewidth + 300, sizeheight + 300
    #cropped = img.crop( ( left, top, width, height ) )
    #cropped.save(str(counter)+'-Q3-C.jpg')
    #counter = counter + 1
    while img.height > sizeheight: 
        left, top, width, height = sizewidth, sizeheight, sizewidth + 300 , sizeheight + 300
        cropped = img.crop( ( left, top, width, height ) )
        cropped.save(str(counter)+'-QX-XIX.jpg')
        sizeheight = sizeheight + 300
        counter = counter + 1
    sizewidth = sizewidth + 300
    counter_height = counter_height + 1
