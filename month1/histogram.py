# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#construct a grayscale histogram

hist=cv2.calcHist([image],[0],None,[256],[0,256])

#matplotlib excepts RGB images so convert and then display the image

plt.figure()
plt.axis("off")

plt.imshow(cv2.cvtColor(image,cv2.COLOR_GRAY2RGB))

#plot the histogram

plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)


cv2.destroyAllWindows()
# normalize the histogram
hist /= hist.sum()
 
# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()