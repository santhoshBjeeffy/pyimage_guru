# import the necessary packages
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image=cv2.imread(args['image'])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(7,7),0)
cv2.imshow("IMAGE",image)
cv2.imshow("BLURRED",blurred)
cv2.waitKey(0)


(T,threshInv)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inverse",threshInv)


#finally we will visualize the masked regions in the image
cv2.imshow("output",cv2.bitwise_and(image,image,mask=threshInv))
cv2.waitKey(0)

cv2.destroyAllWindows()




#apply otsu's thresholding

(T,threshinv)=cv2.threshold(blurred,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold",threshinv)

print("OTSU value {}".format(T))


#finally we can visualize the masked regions of the image

cv2.imshow("output",cv2.bitwise_and(image,image,mask=threshinv))

cv2.waitKey(0)


cv2.destroyAllWindows()

from skimage.filters import threshold_local


thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,15)
cv2.imshow("OPencv mean thresh",thresh)


T=threshold_local(blurred,29,offset=5,method="gaussian")
thresh=(blurred<T).astype("uint8")*255

cv2.imshow("scikit-image mean thresh ",thresh)
cv2.waitKey(0)