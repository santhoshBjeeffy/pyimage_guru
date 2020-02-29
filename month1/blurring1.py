# import the necessary packages
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


#load the image and displays it

image=cv2.imread(args['image'])
cv2.imshow("original",image)

kernelsizes=[(3,3),(9,9),(15,15)]


#loop over all the kernel sizes

for (kx,ky) in kernelsizes:
	blurred=cv2.blur(image,(kx,ky))
	cv2.imshow("Average({},{})	".format(kx,ky),blurred)
	cv2.waitKey(0)

cv2.destroyAllWindows()


for (kx,ky) in kernelsizes:
	blurred=cv2.GaussianBlur(image,(kx,ky),0)
	cv2.imshow("GaussianBlur({},{}".format(kx,ky),blurred)
	cv2.waitKey(0)


cv2.destroyAllWindows()
#loop over kernel sizes and apply median

for k in (3,9,15):
	blurred=cv2.medianBlur(image,k)
	cv2.imshow("median {} ".format(k),blurred)
	cv2.waitKey(0)

cv2.destroyAllWindows()


params=[(11,21,7),(11,41,21),(11,61,39)]

#loop over the diameter,sigma color and sigma space

for (diameter,sigmacolor,sigmaspace)in params:
	#apply bilateral and display the image
	blurred=cv2.bilateralFilter(image,diameter,sigmacolor,sigmaspace)
	title="Blurred d={},sg={},sspace={}".format(diameter,sigmacolor,sigmaspace)
	cv2.imshow("title",blurred)
	cv2.waitKey(0)

cv2.destroyAllWindows()


