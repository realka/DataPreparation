import cv2
import numpy as np
import math
from PIL import Image
import glob, os
import sys


img_matris = []
# gray_matris = []

# w, h = 54000, 270001;
# formatted_matris = [[0 for x in range(w)] for y in range(h)]

# img = cv2.imread('Q3A.1.jpg')
# gray = cv2.imread('Q3A.1.jpg', cv2.IMREAD_GRAYSCALE)


# gray_matris.append(gray)


# np_gray = np.array(gray_matris)

# print(np_img.shape)
# print(np_img.shape)
# print(np_img[0,767,1365,0])

row = 0
file2write=open("out.txt",'r+')

for infile in glob.glob("./allimg/*.jpg"):
    # print(infile)
    strr = ''
    row = row +1
    img = cv2.imread(infile)
    file, ext = os.path.splitext(infile)
    # print(infile)
    label = file.split('\\')
    labelx = label[1].split('.')
    img_matris.append(img)
    np_img = np.array(img_matris)
    print(labelx[0])
    index = 0
    for color in range(3):
        for width in range(300):
            for height in range(300):
                index = index + 1
                strr = strr  +  str(np_img[0,width,height,color]) + ','
    strr = strr + labelx[0]
    file2write.write(strr+ '\n')

file2write.close()

# np.savetxt('data.txt', formatted_matris, delimiter=',',comment=label , fmt='%4e')
