import cv2
import numpy as np 

img = cv2.imread('D:/shared/pyimageguru/images/simpsons_frame0.png')
print('Original Dimensions : ',img.shape)

scale_percent = 45 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",gray)
cv2.waitKey(0)

# threshhold
ret,bin = cv2.threshold(gray,3.8,255,cv2.THRESH_BINARY_INV)

# closing
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)

# invert black/white
inv = cv2.bitwise_not(closing)

cv2.imshow("final_image",inv)

cv2.waitKey(0)