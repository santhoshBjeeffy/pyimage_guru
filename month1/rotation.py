import cv2
import numpy as np 
import imutils
import argparse


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#grab the dimension of the image and calculate the center of the image

(h,w)=image.shape[:2]
(cx,cy)=(w/2,h/2)



#Rotate the image from arbitary point instead from the center

M=cv2.getRotationMatrix2D((50,50),88,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated from arbitary point anf 45 degree",rotated)
cv2.waitKey(0)

(b,g,r)=rotated[10,10]
print("Pixel at (10, 10) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))



#quiz rotate 30 degree clockwise
M=cv2.getRotationMatrix2D((cx,cy),110,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated clockwise 30 degree",rotated)
cv2.waitKey(0)

(b,g,r)=rotated[136,312]
print("Pixel at (136, 312) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))



#rotate the image by 45 degree

M=cv2.getRotationMatrix2D((cx,cy),45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated by 45 degree",rotated)
cv2.waitKey(0)


#Roatate the image by -90 degree

M=cv2.getRotationMatrix2D((cx,cy),-90,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated by -90 degree",rotated)
cv2.waitKey(0)


#Rotate the image from arbitary point instead from the center

M=cv2.getRotationMatrix2D((cx-50,cy-50),88,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated from arbitary point anf 45 degree",rotated)
cv2.waitKey(0)

(b,g,r)=rotated[10,10]
print("Pixel at (10, 10) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))