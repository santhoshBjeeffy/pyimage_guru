# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#load the image and convert in to grayscale

image=cv2.imread(args['image'])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#find the external contours in the image

cnts=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

clone=image.copy()

#loop over the contours

for c in cnts:
	#compute the moments in the contours which will compute the 
	#centroid or center of mass of the region

	M=cv2.moments(c)
	cx=int(M["m10"]/M["m00"])
	cy=int(M["m01"]/M["m00"])

	#draw the center of the contours in the image
	cv2.circle(clone,(cx,cy),10,(0,255,0),-1)


#show the output image

cv2.imshow("Centroids",clone)
cv2.waitKey(0)

cv2.destroyAllWindows()


for (i,c) in enumerate(cnts):
	area=cv2.contourArea(c)
	perimeter=cv2.arcLength(c,True)
	print("contour # {}-- area :{:.2f},perimeter : {:.2f}".format(i+1,area,perimeter))


	#draw the contour on the image
	cv2.drawContours(clone,[c],-1,(0,255,0),2)

	#compute the center of the contour and draw the contour number
	M=cv2.moments(c)
	cx=int(M["m10"]/M["m00"])
	cy=int(M["m01"]/M["m00"])

	cv2.putText(clone, "#{}".format(i+1),(cx-20,cy),cv2.FONT_HERSHEY_SIMPLEX,1.25,(255,255,255),4)

#show the output image
cv2.imshow("Contours",clone)
cv2.waitKey(0)

cv2.destroyAllWindows()


clone=image.copy()

for c in cnts:
	(x,y,w,h)=cv2.boundingRect(c)
	cv2.rectangle(clone,(x,y),(x+w,y+h),(0,255,0),2)

#show the output image

cv2.imshow("Bounding boxes",clone)
cv2.waitKey(0)


#Rotated Bounding boxes

for c in cnts:
	#fit a rotated bounding box and draw the same
	box=cv2.minAreaRect(c)
	box=np.int0(cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box))
	cv2.drawContours(clone,[box],-1,(0,255,0),2)

#show the output image
cv2.imshow("Roatated bounding box is ",clone)
cv2.waitKey(0)

cv2.destroyAllWindows()


#fitting the circle

for c in cnts:
	((x,y),radius)=cv2.minEnclosingCircle(c)
	cv2.circle(clone,(int(x),int(y)),int(radius),(0,255,0),2)


#show the output image
cv2.imshow("Min-enclosing circle",clone)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Fitting an ellipse

for c in cnts:
	if len(c)>=5:
		ellipse=cv2.fitEllipse(c)
		cv2.ellipse(clone,ellipse,(0,255,0),2)


#show the output image

cv2.imshow("Ellipse image",clone)
cv2.waitKey(0)
