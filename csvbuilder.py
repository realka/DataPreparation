import pandas as pd
import glob, os
import numpy as np
import zipfile

# Variables Definition
arr1 = np.empty((2,300*6), dtype=object) # 300 image per class, 6 class
# path = 'filtered'
tip =['train']
folder = ['2x2Closing','2x2Dilation','2x2Erosion+Dilation','2x2Erosion',
          '2x2Opening','4x4Closing','4x4Dilation','4x4Erosion','4x4Opening','Bilateral','Blur',
          'GaussianBlur','GreyMedian','Median','sepFilter']

subfolder =['Q3A','Q3B','Q3C','Q4A','Q4B','Q4C']


for folds in folder:
    for tips in tip:
        counter = 0
        for ad in subfolder:
            for infile in glob.glob(folds+tips+"/"+ad+"/*.jpg", recursive=True):
                # Split Path
                file, ext = os.path.splitext(infile)
                fold,name =file.split("\\")
                print(folds+"./"+ad+"/"+name+ext+"----"+ad)
                arr1[0,counter] = "./"+ad+"/"+name+ext
                arr1[1,counter] = ad
                counter = counter + 1
            # Export to CSV
        results = pd.DataFrame({'label':arr1[1,:] ,'img':arr1[0,:]})
        results.to_csv(folds+tips+'/'+tips+'.csv', index=False)


