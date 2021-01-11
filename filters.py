import math
import cv2
import numpy as np
import random
from PIL import Image
import os
import matplotlib.pyplot as plt

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

subfolder =['Q3A','Q3B','Q3C','Q4A','Q4B','Q4C']
for name in subfolder:
    for x in range(350):

        image = cv2.imrename("Train/"+name+"/"+name+"."+str(x+1)+".jpg")
        #Median#
        #Median#median = cv2.medianBlur(image,5)
        #Median#plt.imsave("Mediantrain/"+name+"/"+name+"."+str(x+1)+".jpg", median,cmap = 'gray')

        #Gabor#
        #Gabor#kernel = cv2.getGaborKernel((15, 15), 2, 0, 20, 1, 10, cv2.CV_32F)
        #Gabor#kernel = cv2.getGaborKernel((300, 300), 1, 0, 0.05, 1, 30, cv2.CV_32F)
        #Gabor#kernel /= math.sqrt((kernel * kernel).sum())
        #Gabor #filtered = cv2.filter2D(image, -1, kernel)
        #Gabor#filtered *= 255
        #Gabor#filtered = filtered.astype(np.float32)
        #Gabor#filtered = filtered.astype(np.float32) * 255
        #Gabor#filtered = filtered.astype(np.float32)
        #Gabor#status = cv2.imwrite("Gtrain/"+name+"/"+name+"."+str(x+1)+".jpg", filtered)
        #Gabor#print(status)

        #bilateralFilter
        #bilateralFilter#bilateral = cv2.bilateralFilter(image,5,150,150)
        #bilateralFilter#image = cv2.namedWeighted(image, 1.5, bilateral, -0.5, 0)
        #bilateralFilter#image = cv2.bilateralFilter(image, 5, 150, 150)
        #bilateralFilter#status = cv2.imwrite("Bilateraltrain/"+name+"/"+name+"."+str(x+1)+".jpg", image)

        #blur
        #blur# blur = cv2.blur(image,(5,5))
        #blur# status = cv2.imwrite("Blurtrain/"+name+"/"+name+"."+str(x+1)+".jpg", blur)

        #gaussianBlur
        #gaussianBlur# gblur = cv2.GaussianBlur(image,(5,5),0)
        #gaussianBlur# status = cv2.imwrite("GaussianBlurtrain/"+name+"/"+name+"."+str(x+1)+".jpg", gblur)

        #boxFilter
        # image=100*(image-np.mean(image))
        # image[np.where(image>255)]=255
        # image=cv2.boxFilter(image,-1,(30,30))
        # image[np.where(image>150)]=255; image[np.where(image<=150)]=0
        # image=cv2.boxFilter(image,-1,(15,15))
        # image[np.where(image>0)]=255
        # image = image.astype(np.float32) / 255
        # status = cv2.imwrite("Boxedtrain/"+name+"/"+name+"."+str(x+1)+".jpg", image)

        #erosion
        # kernel = np.ones((2,2),np.uint8)
        # erosion = cv2.erode(image,kernel,iterations = 1) # Finds fossils and holes
        # dilation = cv2.dilate(erosion,kernel,iterations = 1)  # finds veins
        # opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) # Finds fossils and holes
        # closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) # finds veins
        # grnameient = cv2.morphologyEx(image, cv2.MORPH_GRnameIENT, kernel)
        # tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
        #blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
        # status = cv2.imwrite("2x2Erosion+Dilation_Train/"+name+"/"+name+"."+str(x+1)+".jpg", dilation)
        # status = cv2.imwrite("4x4Dilationtrain/"+name+"/"+name+"."+str(x+1)+".jpg", dilation)
        # status = cv2.imwrite("4x4Openingtrain/"+name+"/"+name+"."+str(x+1)+".jpg", opening)
        # status = cv2.imwrite("4x4Closingtrain/"+name+"/"+name+"."+str(x+1)+".jpg", closing)

        # sepFilter2D
        # kernel = cv2.getGaussianKernel( 15, 2 )
        # twoD = cv2.sepFilter2D(image, -1, kernel, kernel)
        # status = cv2.imwrite("sepFiltertrain/"+name+"/"+name+"."+str(x+1)+".jpg", twoD)

        # Laplacian,Sobelx,Sobely test
        # laplacian = cv2.Laplacian(image,cv2.CV_64F)
        # sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
        # sobely = cv2.Sobel(sobelx,cv2.CV_64F,0,1,ksize=3)
        #
        # abs_sobel64f = np.absolute(sobely)
        # sobel = np.uint8(abs_sobel64f)
        #
        # plt.subplot(2,2,1),plt.imshow(image)
        # plt.title('Original'), plt.xticks([]), plt.yticks([])
        # plt.subplot(2,2,2),plt.imshow(laplacian)
        # plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        # plt.subplot(2,2,3),plt.imshow(sobel)
        # plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        # plt.subplot(2,2,4),plt.imshow(sobely)
        # plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

        print(str(x+1))

        # print (laped)
        # cv2.imshow('image',blur)
        # cv2.imshow('image',image)
        # print(image)
        # print(filtered)

        # plt.figure(figsize=(8,4))
        # plt.subplot(131)
        # plt.axis('off')
        # plt.title('originalimage')
        # plt.imshow(image)
        # plt.subplot(132)
        # plt.title('filtered')
        # plt.imshow(twoD)
        # plt.subplot(133)
        # plt.title('dilation')
        # plt.imshow(dilation)
        # plt.tight_layout()
        # plt.show()
        # k = cv2.waitKey(0)
        # if k == 27:
        #     cv2.destroyAllWindows()


#plt.figure(figsize=(8,3))
#plt.subplot(131)
#plt.axis('off')
#plt.title('image')
#plt.imshow(image, cmap='gray')
#plt.subplot(132)
#plt.title('kernel')
#plt.imshow(kernel, cmap='gray')
#plt.subplot(133)
#plt.axis('off')
#plt.title('filtered')
#plt.imshow(filtered, cmap='gray')
#plt.tight_layout()
#plt.show()
