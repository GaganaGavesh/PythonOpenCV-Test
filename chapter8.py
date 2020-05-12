import cv2
import numpy as np

path = 'Resources/shapes.png'
img = cv2.imread(path)

cv2.imshow("Shapes Image",img)

cv2.waitKey(0)