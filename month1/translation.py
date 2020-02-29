import cv2
import argparse
import imutils
import numpy as np 


#constrct the argument parser to parse the argument

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#load the iamge and show it
image=cv2.imread(args["image"])
cv2.imshow("Image",image)

# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down
M=np.float32([[1,0,25],[0,1,50]])

shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

cv2.imshow("Shifted down and right",shifted)

cv2.waitKey(0)


# now, let's shift the image 50 pixels to the left and 90 pixels up, we
# accomplish this using negative values

N=np.float32([[1,0,-50],[0,1,-90]])

shifted=cv2.warpAffine(image,N,(image.shape[1],image.shape[0]))

cv2.imshow("shifted left and up",shifted)

cv2.waitKey(0)

#Left 100 pixels
shifted=imutils.translate(image,100,100)
cv2.imshow("Imutils_translate",shifted)
cv2.waitKey(0)