import cv2 as cv

img = cv.imread('Photos/forest.jpg')
cv.imshow('forest',img)

#Blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascode
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edge',canny)

#Dilating the image
dilated = cv.dilate(canny,(5,5),iterations=1)
cv.imshow('Dilated',dilated)

#Eroding
eroded = cv.erode(dilated,(5,5),iterations=1)
cv.imshow('Eroded',eroded)

#resize
resized = cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped = img[200:400,50:200]
cv.imshow('Cropped',cropped)

cv.waitKey(0)