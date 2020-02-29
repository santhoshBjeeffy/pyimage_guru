# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2
import imutils
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# grab the image channels, initialize the tuple of colors and the
# figure
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")


#loop over the image channels

for (chan,color) in zip(chans,colors):
	#create the histogram for current channel and plot it
	hist=cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist,color=color)
	plt.xlim([0,256])
	plt.show()
	cv2.waitKey(0)


# let's move on to 2D histograms -- we need to reduce the
# number of bins in the histogram from 256 to 32 so we can
# better visualize the results
fig = plt.figure()
 
# plot a 2D color histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
 
# plot a 2D color histogram for green and red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)
 
# plot a 2D color histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
 
# finally, let's examine the dimensionality of one of the 2D
# histograms
print("2D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))



# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram
hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))
 
# display the image with matplotlib to avoid GUI conflicts on macOS
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))
 
# show our plots
plt.show()




#lor_histograms.pyPython
# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram
hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

# display the image with matplotlib to avoid GUI conflicts on macOS
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))

# show our plots
plt.show()

# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram


hist = cv2.calcHist([image], [0, 1, 2],
	None, [9, 16, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))
 
# display the image with matplotlib to avoid GUI conflicts on macOS
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))
 
# show our plots
plt.show()



#Histogram Equilize

 
# apply histogram equalization to stretch the contrast of our image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(image)
 

# show our images -- notice how the contrast of the second image has
# been stretched
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)
eq=cv2.cvtColor(eq,cv2.COLOR_GRAY2BGR)

(b,g,r)=eq[272,146]
print("Pixel at (272, 146) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
