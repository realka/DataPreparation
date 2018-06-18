import random
from PIL import Image
import os

arr = range(350)
rand = random.sample(arr,50)
ad ="Q4-C"
for x in rand:
    img = Image.open("C:/test/data/validate/"+ad+"/"+str(x+1)+"-"+ad+".jpg")
    img.save("C:/test/data/train/"+ad+"/"+str(x+1)+"-"+ad+".jpg")
    os.remove("C:/test/data/validate/"+ad+"/"+str(x+1)+"-"+ad+".jpg")
    print(str(x+1))
    