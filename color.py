import cv2
import numpy as np

def Onclick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition       
        colors = img[y,x]
        print("BRG Format: ",colors)

img=cv2.imread("image.jpeg")
cv2.namedWindow('TASK WINDOW')
cv2.setMouseCallback('TASK WINDOW',Onclick)
while (1):
    cv2.imshow('TASK WINDOW',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()