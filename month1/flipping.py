# import the necessary packages
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
 
# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

#(b,g,r)=flipped[235,259]
#print("Pixel at (235, 259) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

 
#grab the dimension of the image and calculate the center of the image

(h,w)=flipped.shape[:2]
(cx,cy)=(w/2,h/2)



#Rotate the image from arbitary point instead from the center

M=cv2.getRotationMatrix2D((cx,cy),45,1.0)
rotated=cv2.warpAffine(flipped,M,(w,h))

cv2.imshow("Rotated from arbitary point anf 45 degree",rotated)
cv2.waitKey(0)


# flip the image vertically
flipped_vertical = cv2.flip(rotated, 0)
cv2.imshow("Flipped Vertically", flipped_vertical)

(b,g,r)=flipped_vertical[189,441]
print("Pixel at (189, 441) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))













# flip the image vertically
flipped = cv2.flip(image, 0)
#cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
#cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)