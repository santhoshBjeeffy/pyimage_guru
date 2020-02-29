import numpy as np 
import cv2
import argparse

 #construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Masking allows us to focus only on parts of an image that interest us.
# A mask is the same size as our image, but has only two pixel values,
# 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept. For example,
# let's construct a rectangular mask that displays only the person in
# the image


mask=np.zeros(image.shape[:2],dtype="uint8") 
#We then construct a NumPy array, filled with zeros, with the same width and height as our original image 

cv2.rectangle(mask,(0,90),(290,450),255,-1)

cv2.imshow("mask",mask)


#Apply our mask notice only person from the image is cropped

masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("mask applied to image",masked)
cv2.waitKey(0)



#Now lets make a circular mask with a radius of 100 pixels

mask=np.zeros(image.shape[:2],dtype="uint8")
cv2.circle(mask,(145,200),100,255,-1)
masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Mask",mask)
cv2.imshow("mask applied to the image",masked)
cv2.waitKey(0)

