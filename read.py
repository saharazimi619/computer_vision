import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#img = cv.imread('Photos/cat.jpg')
#cv.imshow('cat',img)

#change color
blank[50:450,100:300] = (0,255,0)
cv.imshow('Green',blank)

#rectangle
cv.rectangle(blank,(100,50),(300,450),(0,0,255),thickness=3)
cv.imshow('Rectangle',blank)

#circle
cv.circle(blank,(blank.shape[1]//2 , blank.shape[0]//2), 40,(255,0,0),thickness=3)
cv.imshow('Circle',blank)

#line
cv.line(blank,(100,50),(300,450),(255,0,0),thickness=3)
cv.imshow('Line',blank)

#text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),2)
cv.imshow('Line Text',blank)

cv.waitKey(0)