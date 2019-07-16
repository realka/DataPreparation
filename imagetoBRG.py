import cv2
import numpy as np

img_matris = []
gray_matris = []
# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 900, 900;
formatted_matris = [[0 for x in range(w)] for y in range(h)]

img = cv2.imread('xxx.jpg')
gray = cv2.imread('xxx.jpg', cv2.IMREAD_GRAYSCALE)

img_matris.append(img)
gray_matris.append(gray)

np_img = np.array(img_matris)
np_gray = np.array(gray_matris)

print(np_img.shape)
# print(np_img.shape)
# print(np_img[0,767,1365,0])
for k in range(3):
    for j in range(300):
        for i in range(300):
            if(k == 0):
                x = 0;
            else:
                x = 300*k;
            formatted_matris[x+j][x+i] =  np_img[0,j,i,k]
                # formatted_matris[j][i] = np_img[0,j,i,k]
        # print(np_img[0,j,i,0])
    # temp = formatted_matris[0][0] +'-'+ k
    # print(temp)
np.savetxt('xxx.jpg.csv', formatted_matris, delimiter=',', fmt='%4d')
    # formatted_matris.append(np_img[0,j,i,0])
# print(formatted_matris)
# np.savetxt("test.csv",formatted_matris,fmt='%4i', delimiter=",")
# a = np.asarray(formatted_matris)
# a.tofile('test.txt',sep=';',format='%4i')
#     print(np_gray[0,0,0])
#     print(np_gray[0,0,0].shape)
    # np.savetxt("test.txt",np_gray[:i,:1])
    # np.savetxt("test.csv",np_gray[:i,:], delimiter=",")
# print(np_img[0])
# ndarray.tofile('test.csv',np_img)
# np.save('test.txt',np_img)

# np.savetxt("test.csv", np_img[0], delimiter=",")
# np.savetxt("test.csv", np_gray[1:1366], delimiter=",")

# print(img)
# print('splitter')
# print(np_img)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
