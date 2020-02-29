import cv2
import numpy as np 
import argparse


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


#load the image and convert in to grayscale

image=cv2.imread(args['image'])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray_Image',image)


#apply a series of erosion

for i in range(0,3):
	eroded=cv2.erode(gray.copy(),None,iterations=i+1)
	cv2.imshow("ERoded{}times".format(i+1),eroded)
	cv2.waitKey(0)

cv2.destroyAllWindows()


#Apply series of dilation

for i in range(0,3):
	dilated=cv2.dilate(gray.copy(),None,iterations=i+1)
	cv2.imshow("Dilated {} times".format(i+1),dilated)
	cv2.waitKey(0)


cv2.destroyAllWindows()
cv2.imshow("original",image)
kernelsizes=[(3,3),(5,5),(7,7)]


#loop over the kernels and apply the "opening" in an image

for kernelsize in kernelsizes:
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
	opening=cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
	cv2.imshow("opening: ({},{}".format(kernelsize[0],kernelsize[1]),opening)
	cv2.waitKey(0)

cv2.destroyAllWindows()
	#loop over the kernels and apply the "closing " in an image


for kernelsize in kernelsizes:
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
	closing=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
	cv2.imshow("Closing :({},{}".format(kernelsize[0],kernelsize[1]),closing)
	cv2.waitKey(0)

cv2.destroyAllWindows()


#Morphological Gradient
#A morphological gradient is the difference between the dilation and erosion.
# It is useful for determining the outline of a particular object of an image:

for kernelsize in kernelsizes:
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelsize)
	gradient=cv2.morphologyEx(gray,cv2.MORPH_GRADIENT,kernel)
	cv2.imshow("Gradient:({},{})".format(kernelsize[0],kernelsize[1]),gradient)
	cv2.waitKey(0)


cv2.getStructuringElement(cv2.MORPH_RECT,(6,5))
