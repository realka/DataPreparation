import random
from PIL import Image
import os



#path = "filtered/"
#folder = ['2x2Closing','2x2Dilation','2x2Erosion+Dilation','2x2Erosion','2x2Opening',
#          '4x4Closing','4x4Dilation','4x4Erosion','4x4Opening','Bilateral','Blur',
#          'GaussianBlur','GreyMedian','Median','sepFilter']
arr = range(350)
path = "data/"
rand = random.sample(arr,50)
folder =['OriginalData']
subfolder = ['Q3A','Q3B','Q3C','Q4A','Q4B','Q4C']
for fold in folder:
    for ad in subfolder:
        for x in rand:
            img = Image.open(path+fold+"train/"+ad+"/"+ad+"."+str(x+1)+".jpg")
            img.save(path+fold+"test/"+ad+"/"+ad+"."+str(x+1)+".jpg")
            os.remove(path+fold+"train/"+ad+"/"+ad+"."+str(x+1)+".jpg")
            print(str(x+1))
