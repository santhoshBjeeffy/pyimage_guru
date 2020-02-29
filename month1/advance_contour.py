import numpy as np 
import cv2
import imutils

image=cv2.imread("D:/shared/pyimageguru/images/tictactoe.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#find all contours in tic-tac board

cnts=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)


#loop over the contours

for (i,c) in enumerate(cnts):
	area=cv2.contourArea(c)
	(x,y,w,h)=cv2.boundingRect(c)


	hull=cv2.convexHull(c)
	hullarea=cv2.contourArea(hull)
	solidity=area/float(hullarea)

	#initialize the character text '?'

	char='?'

	if solidity > 0.9:
		char="0"

	elif solidity >0.5:
		char="x"


	#if the character is not unknown draw it

	if char != "?":
		cv2.drawContours(image,[c],-1,(0,255,0),3)
		cv2.putText(image,char,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1.25,(0,255,0),4)

	print("{} (contour #{}) -- solidity={:2f}".format(char,i+1,solidity))

#show the output image

cv2.imshow("output",image)
cv2.waitKey(0)

cv2.destroyAllWindows()


image=cv2.imread("D:/shared/pyimageguru/images/tetris_blocks.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]

#show the thresh and original image

cv2.imshow("original",image)
cv2.imshow("Threshold",thresh)


#find external contours
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
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

	shape=""

	if aspectratio >=0.98 and aspectratio <=1.02:
		shape="SQUARE"

## if the width is 3x longer than the height, then we have a rectangle
	elif aspectratio >=3.0:
		shape="Rectangle"

	## if the extent is sufficiently small, then we have a L-piece

	elif aspectratio < 0.65:
		shape="L-shape"

	elif solidity > 0.80:
		shape="Z-shape"

	#draw the shape name and image
	cv2.putText(image,shape,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(240,0,159),2)

	#show the contour properties

	print("contour:{}-- aspectratio={:.2f},extent={:.2f},solidity={:.2f}".format(i+1,aspectratio,extent,solidity))

	cv2.imshow("convexHull",hullImage)
	cv2.imshow('image',image)
	cv2.waitKey(0)





