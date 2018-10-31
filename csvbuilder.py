import pandas as pd
import glob, os
import numpy as np

# Variables Definition
arr1 = np.empty((2,300*6), dtype=object) # 300 image per class, 6 class
tip =['Gtrain','Gtest']
add =['Q3A','Q3B','Q3C','Q4A','Q4B','Q4C']

for tips in tip:
    counter = 0
    for ad in add:
        for infile in glob.glob(tips+"/"+ad+"/*.jpg", recursive=True):
            # Split Path
            file, ext = os.path.splitext(infile)
            fold,name =file.split("\\")
            print("./"+ad+"/"+name+ext+"----"+ad)
            arr1[0,counter] = "./"+ad+"/"+name+ext
            arr1[1,counter] = ad
            counter = counter + 1
    # Export to CSV
    results = pd.DataFrame({'label':arr1[1,:] ,'img':arr1[0,:]})
    results.to_csv(tips+'.csv', index=False)
