import numpy as np 
import cv2
import imutils


image=cv2.imread("D:/shared/pyimageguru/images/more_shapes_example.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]

#show the thresh and original image

cv2.imshow("original",image)
#cv2.imshow("Threshold",thresh)


#find external contours
cnts=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
hullImage=np.zeros(gray.shape[:2],dtype="uint8")

for (i,c) in enumerate(cnts):
	area=cv2.contourArea(c)
	(x,y,w,h)=cv2.boundingRect(c)

	aspectratio=w/h 

	extent=area/float(w*h)

	hull=cv2.convexHull(c)
	hullarea=cv2.contourArea(hull)
	solidity=area/float(hullarea)

	cv2.drawContours(hullImage,[hull],-1,255,-1)
	cv2.drawContours(image,[c],-1,(240,0,159),3)

	print("contour:{}-- aspectratio={:.2f},extent={:.2f},solidity={:.2f}".format(i+1,aspectratio,extent,solidity))

	cv2.imshow("convexHull",hullImage)
	cv2.imshow('image',image)
	cv2.waitKey(0)

