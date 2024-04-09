import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat',img)

plt.imshow(img)
plt.show()