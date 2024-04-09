#import the opencv package
import cv2
import matplotlib.pyplot as plt

#read the image
img = cv2.imread('Photos/inception2.jpg')
print(img.shape)

#convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

#load the classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#perform the face detection
face = face_classifier.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=15,minSize=(50,50))

#drawing a bounding box
for (x,y,w,h) in face :
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

#displaying the image    
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.figure(figsize=(20,10))
#plt.imshow(img_rgb)
#plt.axis('off')
#plt.show()
cv2.imshow('figure',img)
cv2.waitKey(0)