import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('cat',img)

#bgr 2 grayscale 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bgr 2 hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#bgr 2 L*A*B
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#bgr 2 rgb
rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
#L*A*B 2 bgr
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB_BGR',lab_bgr)

cv.waitKey(0)
