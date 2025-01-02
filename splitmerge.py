''''''
#sahar azimi
#Taking a BGR photo and turning it a grayscale photo

''''''
import cv2 as cv
import numpy as np

img = cv.imread('photo/cat.jpg')
cv.imshow('cat',img)
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)
cv.waitKey(0)