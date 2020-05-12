import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350

pointsInCard = np.float32([[111,219],[287,188],[154,482],[352,440]]) # np array of flooat/me widiya gana poddak balanna wenawa

pointsToBePlotted = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pointsInCard,pointsToBePlotted)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Cards Original",img)
cv2.imshow("Cards Perspective",imgOutput)

cv2.waitKey(0)
