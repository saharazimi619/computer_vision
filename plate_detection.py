import cv2
import pytesseract
img=cv2.imread('Photos/car4.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
canny =cv2.Canny(blur,125,175)
#cv2.imshow('canny',canny)
contours,hierarchies = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:15]
lp_contours = None
for contour in contours:
    arclength = cv2.arcLength(contour,True)
    approx_dist = 0.01 *arclength
    approx_contour = cv2.approxPolyDP(contour,approx_dist,True)
    if len(approx_contour) == 4:
        lp_contours = approx_contour
        x,y,w,h = cv2.boundingRect(contour)
        lp_crop = gray[y:y+h , x:x+w]
        break

cv2.drawContours(img, [lp_contours],-1,(0,255,0),2)
cv2.imshow('contours draw',img)
pytesseract.pytesseract.tesseract_cmd

cv2.waitKey(0)
