import numpy as np 
import cv2
import argparse
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


cnts=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
clone=image.copy()


for (i,c) in enumerate(cnts):
	M=cv2.moments(c)
	cx=int(M["m10"] / M["m00"])
	cy=int(M["m01"] / M["m00"])

	cv2.circle(clone,(cx,cy),10,(0,255,0),-1)
	print("centroid {}={},{}".format(i+1,cx,cy))
	


cv2.imshow("centroids",clone)
cv2.waitKey(0)
#print("centroid {}={},{}".format(i+1,cx,cy))


#Area of the circle

for(i,c)in enumerate(cnts):
	area=cv2.contourArea(c)
	perimeter=cv2.arcLength(c,True)
	print("Contour # {}--area:{:2f},perimeter:{:.2f}".format(i+1,area,perimeter))
	#print("centroid {}={},{}".format(i+1,cx,cy))

	#draw the contours on the image
	cv2.drawContours(clone,[c],-1,(0,255,0),2)
	#compute the center of the contour and draw the contour number
	M=cv2.moments(c)
	cx=int(M["m10"] / M["m00"])
	cy=int(M["m01"] / M["m00"])

	cv2.putText(clone, "#{}".format(i+1),(cx-20,cy),cv2.FONT_HERSHEY_SIMPLEX,1.25,(255,255,255),4)

#show the output image
cv2.imshow("Contours",clone)
cv2.waitKey(0)


#draw the bounding boxes

clone=image.copy()

for(i,c)in enumerate(cnts):
	(x,y,w,h)=cv2.boundingRect(c)
	cv2.rectangle(clone,(x,y),(x+w,y+h),(0,255,0),2)
	print("Bounding box numbers={},x={},y={},w={},h={}".format(i+1,x,y,w,h))

cv2.imshow("Bounding box image",clone)
cv2.waitKey(0)


#minimum closing circle

for (i,c) in enumerate(cnts):
	((x,y),radius) =cv2.minEnclosingCircle(c)
	cv2.circle(clone,(int(x),int(y)),int(radius),(0,255,0))
	print("radius of mimimum enclosing circle i:{}={}".format(i+1,radius))

cv2.imshow("min enclosing circle",clone)
cv2.waitKey(0)
