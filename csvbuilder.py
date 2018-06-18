import pandas as pd
import glob, os
from PIL import Image
import fnmatch
import numpy as np

arr1 = np.empty((2,300*6), dtype=object)
#name = "retinex"
tips ="/train/"
counter = 0
for infile in glob.glob("path/csvbuilder"+tips+"/*.jpg", recursive=True): 
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    #arr.append(im.split("/"))
    a0,a1,a2,a3,a4,a5,a6,a7,a8=file.split("/")
    t1,t2=a8.split("\\")
    t3=("images"+tips+t1+"/"+t2+".jpg")
    print(t1+"----"+t3)
    arr1[0,counter] = t3
    arr1[1,counter] = t1
    counter = counter + 1
results = pd.DataFrame({'img':arr1[1,:] ,'label':arr1[0,:]})
results.to_csv('train.csv', index=False) #simple output (retinex1-Q3-A.jpg)