import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
imgResize = cv2.resize(img,(300,200))
print(img.shape)#(462, 623, 3) meken image eke height width color chennels BGR
print(imgResize.shape)

#image is a metric of pixels, so in the crop we have to define the height range and width range

imgCropped = img[0:200,200:500] #top right corner eken thama patan ganne (0,0) issella tynne height eka,dewaniyata width eka



cv2.imshow("Image Lambo",img)
cv2.imshow("Image LamboResized",imgResize)
cv2.imshow("Image LamboCropped",imgCropped)

cv2.waitKey(0)