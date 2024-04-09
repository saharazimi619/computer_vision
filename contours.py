import cv2 as cv
import numpy as np

img = cv.imread('Photos/forest.jpg')
cv.imshow('boston',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#canny = cv.Canny(gray,125,175)
#cv.imshow('Canny Edges',canny)

#blur = cv.GaussianBlur(canny,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)

contours,hierarchies = cv.findContours(gray,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)}contour(s)found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Dawn',blank)

cv.waitKey(0)