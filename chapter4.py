import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
# img[:] = 255,255,255 # mulu image ekatama pata apply wenna ona nisa : eka mada dala tynawa/range ekak pata karanna ona nam agayan danawa
#img[0:200,200:500] = 255,255,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)# line eka dana image eka,start,end,color,thickness
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),2)
cv2.putText(img," OPENCV ",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3) # Thunweni paraeter eka kothana indanda patanganne kiyana eka
                                                                             # 4 font eka(opencv eke tynawa font tikak),
                                                                             # 5 scale eka,6 color eka,7 thama thickness eka

cv2.imshow("Image",img)

cv2.waitKey(0)