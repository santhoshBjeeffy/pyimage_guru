import numpy as np 
import cv2


rectangle=np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)

cv2.imshow("Rectangle",rectangle)

cv2.waitKey(0)

#secondly lets draw a circle

circle=np.zeros((300,300),dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("circle",circle)

cv2.waitKey(0)


bitwiseAnd=cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND",bitwiseAnd)


bitwiseor=cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR",bitwiseor)


bitwisexor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR",bitwisexor)


bitwisenot=cv2.bitwise_not(rectangle,circle)
cv2.imshow("NOT",bitwisenot)

cv2.waitKey(0)