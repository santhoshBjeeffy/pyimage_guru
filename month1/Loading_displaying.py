import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
print("width of the image is %d pixels"%(image.shape[1]))
print("Height of the image is %d pixels"%(image.shape[0]))
print("channels %d"%(image.shape[2]))


cv2.imshow("Image",image)
cv2.waitKey(0)


#Hardcoding path of the image
#image = cv2.imread("path/to/your/image.jpg")



cv2.imwrite("newimage.jpg",image)