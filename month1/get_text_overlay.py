# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    img = cv2.imread('D:/shared/pyimageguru/images/simpsons_frame0.png')
    print('Original Dimensions : ',img.shape)

    scale_percent = 45 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
     
    print('Resized Dimensions : ',resized.shape)
     
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray image",gray)
    cv2.waitKey(0)

    # threshhold
    ret,bin = cv2.threshold(gray,3.8,255,cv2.THRESH_BINARY_INV)

    # closing
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)

    # invert black/white
    output = cv2.bitwise_not(closing)
    cv2.imshow("final output",output)
    cv2.waitKey(0)

     
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('D:/shared/pyimageguru/images/simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################

