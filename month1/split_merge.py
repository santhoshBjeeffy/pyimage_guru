import numpy as np 
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!

image=cv2.imread(args["image"])
(B,G,R)=cv2.split(image)

#show each channels individually

cv2.imshow("Red",R)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)

cv2.waitKey(0)

#merge the image back togetther

merged=cv2.merge([B,G,R])
cv2.imshow("merged",merged)
cv2.waitKey(0)

cv2.destroyAllWindows()


(b,g,r)=image[5,80]
#print("Pixel at (225, 111) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
print("pixel at (94,180) is b={b},g={g},r={r}".format(b=b,g=g,r=r))