import cv2
import argparse


#construct the argument parser and parse the arguments

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path of the image")
args=vars(ap.parse_args())

#load the image,grab its dimension and show it

image=cv2.imread(args["image"])
(h,w)=image.shape[:2]
cv2.imshow("Originaal",image)
cv2.waitKey(0)

#images are just numpy array


(b,g,r)=image[225,111]
print("Pixel at (225, 111) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))


(b,g,r)=image[40,50]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

#print("pixel at (0,0)-Red: {r}, Green:{g}, Blue:{b} ".format(r=r,g=g,b=b))

#now,lets change the value of the pixel at (0,0) and make it red

image[244,344]=(0,0,255)
(b,g,r)=image[244,344]

print("pixel at (244,344)- Red:{r},Green:{g},Blue:{b}".format(r=r,g=g,b=b))


#compute the center of the image which is simply width and height divided by 2

(cx,cy)=(w//2, h//2)

#since it is numpy array we can just slice and get the chunks of image
t1=image[0:cy,0:cx]
cv2.imshow("Left part of image",t1)
cv2.waitKey(0)


#similarly will grab top-right,bottom left and bottom right

tr=image[0:cy,cx:w]
br=image[cy:h,cx:w]
bl=image[cy:h,0:cx]

cv2.imshow("top-right",tr)
cv2.waitKey(0)
cv2.imshow("bottom-left",bl)
cv2.waitKey(0)
cv2.imshow("bottom-right",br)

cv2.waitKey(0)



#now make the bottom left region as a green color
image[cy:h,0:cx]=(255,0,0)

cv2.imshow("Greencolor_Bottom_left",image)
cv2.waitKey(0)

(b,g,r)=image[225,111]
print("Pixel at (225, 111) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
