# import the necessary packages
import argparse
import imutils
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#aspect ratio is more important in resizing the image 

r=500/image.shape[1]
dim= (500,int(image.shape[0]*r))


#perform the resize of the image

resized=cv2.resize(image,dim,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized (width)",resized)
cv2.waitKey(0)

(b,g,r)=resized[74,20]
print("Pixel at (74, 20) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# what if we wanted to adjust the height of the image? We can apply
# the same concept, again keeping in mind the aspect ratio, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels

r= 376/resized.shape[0]
dim=(int(resized.shape[1] * r),376)

#perform resizing

resized=cv2.resize(resized,dim,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized(height)",resized)
cv2.waitKey(0)

(b,g,r)=resized[367,170]
print("Pixel at (367, 170) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))


# of course, calculating the ratio each and every time we want to resize
# an image is a real pain -- let's create a  function where we can specify
# our target width or height, and have it take care of the rest for us.
'''resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

	
resized = imutils.resize(image, height=50)

'''