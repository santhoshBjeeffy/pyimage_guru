#In this lesson, we’ll review the three most basic methods to draw shapes: cv2.line , cv2.rectangle , and cv2.circle .

import cv2
import numpy as np 

#initialize our canvas with 300,300 with 3 channels with black background
#img = np.zeros([height, width, 3], dtype=np.uint8)

canvas=np.zeros((300,300,3),dtype="uint8")  #300*300 image

#draw green line from top left corner of our canvas to the bottom right

green=(0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("canvas",canvas)

cv2.waitKey(0)

#now,draw a 3 pixel thick red line from top-right corner to the bottom right
red=(0,0,255)
cv2.line(canvas,(300,0),(0,300),red,10)
cv2.imshow("canvas_Red",canvas)
cv2.waitKey(0)


#draw a 50x50 pixel square starting at 10x10 and ending at 60x60
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("square",canvas)
cv2.waitKey(0)

#draw another rechange with red and thickness 3
cv2.rectangle(canvas,(100,100),(200,200),red,3)
cv2.imshow("red square",canvas)
cv2.waitKey(0)


#lets draw a last rectangle blue and filled in

blue=(255,0,0)
cv2.rectangle(canvas,(200,50),(225,125), blue, -1)
cv2.imshow("blue rectangle",canvas)
cv2.waitKey(0)


#circles

#reset our canvas and draw a circle

canvas=np.zeros((300,300,3),dtype="uint8")
(centerx,centery)=(canvas.shape[1]//2,canvas.shape[0]//2)
white=(255,255,255)

for r in range(0,175,25):
	cv2.circle(canvas,(centerx,centery),r,white)


cv2.imshow("canvas",canvas)
cv2.waitKey(0)


#lets draw 25 random circles

for i in range(25):
	radius=np.random.randint(5,high=200)
	color=np.random.randint(0,high=256,size=(3,)).tolist()
	pt=np.random.randint(0,high=300,size=(2,))

	cv2.circle(canvas,tuple(pt,),radius,color,-1)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)




image=cv2.imread("D:/shared/pyimageguru/images/florida_trip.png")

#draw a circle around my face,two filled in circles covering my eyes,and a rectangle surrounded by mouth

cv2.circle(image,(168,188),90,(0,0,255),2)
cv2.circle(image,(150,164),10,(0,0,255),-1)
cv2.circle(image,(192,174),10,(0,0,255),-1)
cv2.rectangle(image,(134,200),(186,218),(0,0,255),-1)

#show the output image
cv2.imshow("output",image)
cv2.waitKey(0)