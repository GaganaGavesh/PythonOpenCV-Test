import cv2
import numpy as np
# print("package imported")
####################################################################
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("output",img)
# cv2.waitKey(0)
####################################################################
cap = cv2.VideoCapture(0)
#methana api open wena window eke size eka denna ona 3 width 4 height
cap.set(3,640)
cap.set(4,480)
cap.set(10,500)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#############################################################################
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = cap.read()#success kiyanne hariyata image eka read kalada nadda kiyala boolean walin ewana variable ekak
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

############################################################################
kernal = np.ones((3,3),np.uint8)

img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)# kernal eka thama dewani parameter eka,ewa odd numbers walin thama tyenna ona
                                           # 3,3 and 5,5 wage enna ona,dewaniyata tynne sigma x kiyala value ekak,mewa surface eke tyna characteristics
                                           # iyala thama therenne

imgCanny = cv2.Canny(img,150,100) #canny kiyanne edge dectector 1k,mehe threshold values thama ilakkam walin dila tynnee
                                  #threshold value eka wadi karanakota edges ganana adu wenaa
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDilation,kernal,iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
